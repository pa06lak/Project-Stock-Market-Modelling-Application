import pandas as pd
from replit import db
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import *
from dataHandling import dataHandling

class machineLearning: 
  def __init__(self,name):
    self.name = name
    self.increase = True
    self.precisionScore = 0
    self.predictionValue = 0
    self.dateToday = 0
    self.fileName = ""
    if self.name == "APPL":
      self.actualName = "APPLE"
      self.fileName = "apple.png"
    elif self.name == "KO":
      self.actualName = "Coca Cola"
      self.fileName = "cola.png"
    elif self.name == "CVX": 
      self.actualName = "Chevron Corporations"
      self.fileName = "chevron.png"
    
  def trainData(self, splitArray):
    #here I have done another API calling
    #This is to get the next stock values being the target
    stock = yf.Ticker(self.name)
    stock = stock.history(period = 'max')
    del stock ["Dividends"]
    del stock["Stock Splits"]
    stock["Tomorrow"] = stock["Close"].shift(-1)
    testDataArray = splitArray[0]
    stock["Target"] = stock["Tomorrow"] > stock["Close"].astype(int)
    #this will show if the stock is increasing with 1 or not with zero
    keyList = []
    for key in db: 
      keyList.append(key)
    start = keyList[0]
    end = keyList[len(keyList)-1]
    originalStock = stock
    stock = stock.loc[start:end].copy()
    print(stock)
    predictionValue = self.trainModel(splitArray, stock, originalStock)
    return predictionValue

  def trainModel(self, splitArray, stock, originalStock): 
    #I will need to research more about random forest classifiers
    model = RandomForestClassifier(n_estimators=250, min_samples_split=65, random_state = 1)
    #Using the arrays that I have created from before to split data
    train = splitArray[0]
    validate = splitArray[1]
    train = stock.loc[train[0]:train[len(train)-1]].copy()
    validate = stock.loc[validate[0]: validate[len(validate)-1]].copy()
    predictors = ["Close", "Volume", "Open", "High", "Low"]
    combined = self.predict(train, validate, predictors, model)
    predictions = self.evaluateModel(stock, model, predictors, originalStock)
    print(predictions["Predictions"].value_counts())
    print(precision_score(predictions["Target"], predictions["Predictions"]))
    print(predictions["Target"].value_counts()/predictions.shape[0])
    self.precisionScore = (precision_score(predictions["Target"], predictions["Predictions"]))
    #needed to show the user how accurate my model is
    predictionValue = self.optimisation(originalStock)
    self.save(model)
    return predictionValue
  
  def evaluateModel(self, data, model, predictors, originalStock, start = 2500, step = 250): 
    all_predictions = []
    for i in range(start, originalStock.shape[0], step): #Taking each year and generating predictions
      #It is not even going into the for loop
      train = originalStock.iloc[0:i].copy() #splitting the data into training and testing
      validate = originalStock.iloc[i: (i + step)].copy()
      predictions = self.predict(train, validate, predictors, model) #uses the previous 
      #data of the years to predict the next years data
      all_predictions.append(predictions)
    return pd.concat(all_predictions)
    
  def predict(self, train, validate, predictors, model): 
    #Here I have created a repeatable function that I will predict the stock trends
    model.fit(train[predictors], train["Target"])
    preds = model.predict(validate[predictors]) #This will take the probability of the model predicting either a increase or decrease in the stock price
    preds[preds >= 0.65] = 1 #so if the probability is greater than 0.6 for being a one 
    preds[preds < 0.65] = 0 #else it will be zero
    preds = pd.Series(preds, index = validate.index, name = "Predictions")
    combined = pd.concat([validate["Target"], preds], axis = 1)
    return combined
    
  def save(self,model): 
   print("this has come")
   fileName = "model.sav"
   joblib.dump(model, fileName)
    
  def load(self):
    fileName = "model.sav"
    loaded_model = joblib.load(fileName)
    return loaded_model
    
  def optimisation(self, originalStock):
    horizons = [2, 5, 60, 300, 500,1000] #these are the ranges that I am testing for
    #these are 2 days, one week, one month, 250 days and 4 years
    #This could mean that if the market is decreasing then it could increase or vice versa
    new_predictors = [] # hold the new columns that we will create
    for horizon in horizons: 
      rolling_averages = originalStock.rolling(horizon).mean()
      ratio_column = f"Close_Ratio_{horizon}"
      originalStock[ratio_column] = originalStock["Close"] / rolling_averages["Close"]
      #This is will the ratio of the close today and the close of each time frame of the horizon
      trend_column = f"Trend_{horizon}" #This is needed to see if the stock price would go up or not
      originalStock[trend_column] = originalStock.shift(1).rolling(horizon).sum()["Target"]
      #sum of the number of days the stock price went up
      new_predictors += [ratio_column, trend_column]

    #generating the predictions using a dataframe
    print(originalStock)
    df = pd.DataFrame(originalStock)
    print(df)
    lastRow = df.iloc[-1]
    secondToLast = df.iloc[-2]
    difference = abs(float(secondToLast.iloc[3]) - float(lastRow.iloc[3]))
    self.increase = lastRow.iloc[6]
    print(self.increase)
    if self.increase: 
      predictionValue = float(lastRow.iloc[3]) + difference
    else: 
      predictionValue = float(lastRow.iloc[3]) - difference
    self.predictionValue = predictionValue
    
    originalStock = originalStock.dropna()
    stringOriginalStock = originalStock.to_string(header = "False", index = "False")
    return self.predictionValue

  def makeCoordinates(self, predictionValue): 
    nextDayPrediction = predictionValue
    print(nextDayPrediction)
    dates = []
    closed = []
    print("This is working")
    # Sample data
    for key in db: 
        rowList = db[key].strip().split(',')
        dates.append(key)
        close = rowList[4]  # Assuming the close price is at index 4
        close = close[2:-1]  # Remove any unwanted characters from the close price
        closed.append(float(close))

    # Creating a dictionary for DataFrame
    data = {'Date': dates, 'Closed': closed}

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime type
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Closed'], marker='o', linestyle='-', label='Close Price') #plots all of the historical data
    plt.scatter(df['Date'].iloc[-1] + pd.Timedelta(days=1), nextDayPrediction, color='red', label='Predicted Next Day Close Price') #plots the one point #timeDelta -> converts into seconds and stores as int
    plt.plot([df['Date'].iloc[-1], df['Date'].iloc[-1] + pd.Timedelta(days=1)], [df['Closed'].iloc[-1], nextDayPrediction], color='red', linestyle='-')  #joins that one point
    Title = "Close Price Over Time for Stock" + " " + self.name
    plt.title(Title)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate date labels for better readability
    plt.tight_layout()
    #plt.show()
    print("something here, this is where the graph has been drawn")
    plt.savefig(self.fileName)
    print("this is done")
    return True

  def showGraph(self): 
    graph = mpgraph.imread(self.fileName)
    # Display the figure
    plt.imshow(graph)
    plt.show()
  
    
    


