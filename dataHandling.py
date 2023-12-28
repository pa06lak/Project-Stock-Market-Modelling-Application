from database import Database
import pandas as pd
from replit import db
import math
import statistics

class dataHandling: #inherits from the main class
  def __init__(self, sorted, outlier, normalised, scaled, outlierthresholdUpper, outlierThresholdLower): 
    self.sorted = sorted
    self.outlier = outlier
    self.normalised = normalised #boolean
    self.scaled = scaled
    self.outlierthesholdUpper = outlierthresholdUpper
    self.outlierThresholdLower = outlierThresholdLower
    
  def sortTheData(self,Length):
    row, cols = (Length-2,2)
    sortArray = [[0 for i in range(cols)] for j in range(row)]

    i = -1
    indexer = 0
    for key in db.keys(): 
      counter = 0
      total = 0
      i = i + 1
      indexer = indexer + 1
      for element in db[key].strip().split(','): 
        counter = counter + 1
        if counter == 1: 
          date = element[2:-1]
        if counter != 1 and counter != 7: 
          newElement = element[2:-1]
          total = total + float(newElement)
        elif counter == 7: 
          mean = total / 5
      sortArray[i][0] = date
      sortArray[i][1] = mean
    realArray = sortArray
    arrayStocks = self.quickSort(sortArray,0,len(sortArray)-1)
    self.outlierCondition(arrayStocks, indexer, realArray)
    
  def missingValuesCheck(self): 
    pass
  def accomodatingMissingValues(self): 
    pass


  
  def outlierCondition(self,arr, num, unsortedArray): 
    df = pd.DataFrame(arr) #this creates a dataframe of all the data
    standardDeviation = df[1].std() #
    print(standardDeviation)
    mean = statistics.mean(df[1])
    print(mean)
    medianIndex = math.ceil(num/2)
    lowerquartileIndex = math.ceil(num*3/4)
    upperquartileIndex = math.ceil(num*1/4)
    #an outlier is determined by being four standard deviations away from the mean
    self.outlierthesholdUpper = mean + int(4 * standardDeviation)
    self.outlierthesholdLower = mean + int(4 * standardDeviation)
    self.outlierCheck(unsortedArray,num)


  
  def outlierCheck(self,arr,num):
    for valueInArray in range(num): 
      toReplaceArray = []
      toCheckValue = arr[valueInArray][1]
      print(toCheckValue)
      set = True
      if toCheckValue > self.outlierthesholdUpper or toCheckValue < self.outlierthesholdLower: 
        set = False
      db[arr[valueInArray][0]] = [arr[valueInArray][1],set]
      #Here I will need to change this because this is causing me an error. 
  def transformation(self): 
    pass
  def dataLabeller(self): 
    pass
  def qualityCheck(self): 
    pass
  def quickSort(self, arr, start, end): 
      if start >= end:
          return
      pivot = arr[start][1] #first element is the pivot
      leftpointer = start
      rightpointer = end
      while leftpointer < rightpointer:
          while arr[leftpointer][1] < pivot: 
              leftpointer += 1
          while arr[rightpointer][1] > pivot:
              rightpointer -= 1
          if arr[leftpointer][1] == arr[rightpointer][1]: 
            if arr[leftpointer][1] <= pivot: 
              leftpointer += 1
            elif arr[rightpointer][1] > pivot: 
              rightpointer -= 1
          if leftpointer <= rightpointer:
              arr[leftpointer][1], arr[rightpointer][1] = arr[rightpointer][1], arr[leftpointer][1]
              leftpointer += 1
              rightpointer -= 1
      #value for partition
      index = rightpointer
      #recursion for parition - right partition and left partition
      self.quickSort(arr,start, index-1)
      self.quickSort(arr, index+1, end)
      return arr