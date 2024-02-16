from database import Database
import pandas as pd
from replit import db
import math
import statistics


class dataHandling:  #inherits from the main class

  def __init__(self):
    self.sorted = False
    self.outlier = 0
    self.outlierthesholdUpper = 0
    self.outlierThresholdLower = 0
    self.standardDeviation = 0

  def sortTheData(self, Length):
    row, cols = (Length - 2, 2)
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
    arrayStocks = self.quickSort(sortArray, 0,     
    len(sortArray) - 1)
    self.outlierCondition(arrayStocks, indexer, realArray)

  def outlierCondition(self, arr, num, unsortedArray):
    df = pd.DataFrame(arr)  #this creates a dataframe of all the data
    standardDeviation = df[1].std()  #
    self.setStandardDeviation(standardDeviation)
    mean = statistics.mean(df[1])
    #print(mean)
    medianIndex = math.ceil(num / 2)
    lowerquartileIndex = math.ceil(num * 3 / 4)
    upperquartileIndex = math.ceil(num * 1 / 4)
    #an outlier is determined by being four standard deviations away from the mean
    self.outlierthesholdUpper = mean + int(4 * standardDeviation)
    self.outlierthesholdLower = mean + int(4 * standardDeviation)
    self.outlierCheck(unsortedArray, num)

  def outlierCheck(self, arr, num):
    #for key in db.keys():
    #del db[key]
    for valueInArray in range(num):
      toReplaceArray = []
      toCheckValue = arr[valueInArray][1]
      set = True
      if toCheckValue > self.outlierthesholdUpper or toCheckValue < self.outlierthesholdLower:
        set = False
    keyList = []
    keys = db.keys()
    for key in db.keys():
      if key not in keyList:
        keyList.append(key)
      else:
        del db[key]
        print("I have deleted", key)

  def quickSort(self, arr, start, end):
    if start >= end:
      return
    pivot = arr[start][1]  #first element is the pivot
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
        arr[leftpointer][1], arr[rightpointer][1] = arr[rightpointer][1], arr[
            leftpointer][1]
        leftpointer += 1
        rightpointer -= 1
    #value for partition
    index = rightpointer
    #recursion for parition - right partition and left partition
    self.quickSort(arr, start, index - 1)
    self.quickSort(arr, index + 1, end)
    return arr

  def getStandardDeviaton(self): 
    return self.standardDeviation
  def setStandardDeviation(self, SD):
    self.standardDeviation = SD

  def getoutlierthresholdUpper(self): 
    return self.outlierthesholdUpper
  def setoutlierthresholdUpper(self, upper): 
    self.outlierthreholdUpper = upper

  def getoutlierthresholdLower(self): 
    return self.outlierthesholdLower
  def setoutlierthresholdLower(self, lower): 
    self.outlierthreholdLower = lower

  def getOutlier(self): 
    return self.outlier
  def setOutlier(self, outlier):
    self.outlier = outlier
    


    
