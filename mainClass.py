
from webScraping import webScraping
from dataHandling import dataHandling

class Main: 
  def __init__(self, URL, dataTempStorage, nameOfStock, Date):
    #Question: do I need my machine learning model here
    self.URL = URL
    self.dataTempStorage = dataTempStorage
    self.nameOfStock = nameOfStock
    self.Date = Date
    self.data = []
  def dataRetrieval(self): # Retrieves data from the URL through web-scraping
    webScraping(self.URL, self.dataTempStorage, self.nameOfStock, self.Date).dataRetrieval()
  def databaseAccess(self): # Accesses the database to store the data
    pass
  def analysis(self): # Analyzes the data
    pass
  def validation(self): # Validates the data
    pass
  def startUserInterface(self): # Starts the user interface
    pass
  def generatePredictions(self): # Generates predictions
    pass
  def shutDown(self): # Shuts down the program
    pass
  def loadData(self): # Loads data from the database
    pass
  def dataHandling(self,Length): 
    dataHandling(False, None, False, False, None, None).sortTheData(Length)

