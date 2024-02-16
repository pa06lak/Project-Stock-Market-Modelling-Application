from replit import db
from sklearn import preprocessing

class Database: 
  def __init__(self, nameOfStock): 
    self.nameOfStock = nameOfStock

  def createDatabase(self): 
    for key in db.keys(): 
       del db[key]
    tempStore = [] #temp list storage for the row 
    file = open("webScrape.txt", "r")
    counter = 0
    lengthOutput = 0
    dateArray = []
    for row in file: 
      lengthOutput = lengthOutput + 1
      rowList = row.strip().split(',')
      tempStore.append(rowList)
      date = tempStore[counter][0]
      if counter != 0 and counter != 1: 
        date = date[2:-1]
        dateArray.append(date)
        db[date] = row
      counter = counter + 1
    return lengthOutput

  def add(self, key, value): #key = date, value = stock price
    #here a new key is needed
    db [key] = value
  def retrieval(self, key): 
    return db[key]
  def change(self, key, value): 
    #here an existing key is needed
    if key in db: 
      db [key] = value
    else: 
      print("error")
  def delete(self, key): 
    del db [key]

  def splitData(self): 
    dataIndexed = []
    file = open("webScrape.txt", "r")
    outerCounter = 0
    innerCounter = 0
    for line in file: 
      if outerCounter == 0 or outerCounter == 1: #not needed data points
        pass
      else: 
        dataIndexed.append(line[2:12]) #created a list with all the dates parsed so there is no need for indexing
        innerCounter = innerCounter + 1 #number of elements
      outerCounter = outerCounter + 1
    testData = int(innerCounter/2) 
    validationData = int(testData * 1/3) 
    evaluationData = int(testData * 2/3) 
    diff = innerCounter - (testData + validationData + evaluationData) 
    evaluationData = int(evaluationData + diff)
    testingDataArray = dataIndexed[0:testData]
    validationDataArray = dataIndexed[testData: validationData+testData]
    evaluationDataArray = dataIndexed[validationData + testData: evaluationData + validationData + testData]
    #splitting the list and creating sub-lists
    return testingDataArray, validationDataArray, evaluationDataArray
  
    