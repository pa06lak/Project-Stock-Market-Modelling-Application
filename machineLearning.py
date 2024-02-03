import pandas as pd
from replit import db
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
import matplotlib as plt
import joblib

class machineLearning: 
  def __init__(self):
    self.name = "AAPL"
    
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
    self.trainModel(splitArray, stock, originalStock)

  def trainModel(self, splitArray, stock, originalStock): 
    #I will need to research more about random forest classifiers
    model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state = 1)
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
    self.optimisation(originalStock)
    print("Something")
  
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
    preds[preds >= 0.6] = 1 #so if the probability is greater than 0.6 for being a one 
    preds[preds < 0.6] = 0 #else it will be zero
    preds = pd.Series(preds, index = validate.index, name = "Predictions")
    combined = pd.concat([validate["Target"], preds], axis = 1)
    return combined
    
  def retrain(self): 
    pass
    
  def save(self,model): 
   fileName = "model.sav"
   joblib.dump(model, fileName)
  def load(self, fileName): 
    loaded_model = joblib.load(fileName)
    return loaded_model
    
  def optimisation(self, originalStock):
    horizons = [2, 5, 60, 250, 1000] #these are the ranges that I am testing for
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
    print(originalStock)
    print("Something")
    originalStock = originalStock.dropna()
    stringOriginalStock = originalStock.to_string(header = "False", index = "False")
    file = open("newPredictions.txt", "w")
    file.write(stringOriginalStock)
#next time I need to get an output of what I am seeing in my text file 
#see if my stock is able to be written to my file
    file.close()
  
    
  def updateModel(self): 
    pass
  def interpretModelPrecitions(self): 
    pass
  def makeCoordinates(self): 
    pass


