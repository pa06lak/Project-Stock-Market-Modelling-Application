
from webScraping import webScraping
from dataHandling import dataHandling
from database import Database
from machineLearning import machineLearning

class Main: 
  def __init__(self, nameOfStock):
    #Question: do I need my machine learning model here
    self.nameOfStock = nameOfStock
    self.data = []
  def dataRetrieval(self): # Retrieves data from the URL through web-scraping
    webScraping(self.nameOfStock).dataRetrieval()
  def databaseAccess(self): # Accesses the database to store the data
    pass
  def validation(self): # Validates the data
    pass
  def startUserInterface(self): # Starts the user interface
    pass
  def trainModel(self, splitArray): # Generates predictions
    predictionValue = machineLearning(self.getStock()).trainData(splitArray)
    return predictionValue
  def shutDown(self): # Shuts down the program
    quit()
  def loadData(self): # Loads data from the database
    pass
  def dataHandling(self,Length): 
    dataHandling().sortTheData(Length)
    arrays = self.database()
    return arrays
  def database(self): 
    arrays = Database(self.getStock()).splitData()
    return arrays
  def generatePredictions(self, predictionValue): 
    machineLearning(self.getStock()).makeCoordinates(predictionValue)
    print("the function has ended")
    return True
  def getGraph(self): 
    machineLearning(self.getStock()).showGraph()
  def getStock(self): 
    return self.nameOfStock



def analysis(self): # Analyzes the data
  pass
    
  

