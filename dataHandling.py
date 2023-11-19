from database import Database
import pandas as pd
from replit import db

class dataHandling: #inherits from the main class
  def __init__(self, sorted, outlier, normalised, scaled, outlierthresholdUpper, outlierThresholdLower): 
    self.sorted = sorted
    self.outlier = outlier
    self.normalised = normalised #boolean
    self.scaled = scaled
    self.outlierthesholdUpper = outlierthresholdUpper
    self.outlierThresholdLower = outlierThresholdLower
  def sortTheData(self):
    storeArray = []
    for key in db.keys(): 
      counter = 0
      total = 0
      for element in db[key].strip().split(','): 
        counter = counter + 1
        if counter != 1 and counter != 7: 
          print("*", counter, "")
          newElement = element[2:-1]
          print(newElement)
          total = total + float(newElement)
        elif counter == 7: 
          print(total, "this is the total")
          mean = total / 5
          print(mean, "this is the mean")
  
  def missingValuesCheck(self): 
    pass
  def accomodatingMissingValues(self): 
    pass
  def outlierCondition(self): 
      pass
        
  def outlierCheck(self): 
    pass
  def transformation(self): 
    pass
  def dataLabeller(self): 
    pass
  def qualityCheck(self): 
    pass
  def linkToDatabase(self): 
    pass
  def quickSort(self): 
    pass