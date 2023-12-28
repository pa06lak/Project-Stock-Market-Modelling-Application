from replit import db

class Database: 
  def __init__(self, nameOfStock): 
    self.nameOfStock = nameOfStock

  def createDatabase(self): 
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
    print(lengthOutput)
    return lengthOutput

  def dataIndexing(self): 
    pass
  def backUp(self): 
    pass
  def add(self): 
    pass
  def retrieval(self): 
    pass
  def change(self): 
    pass
  def repeatedValue(self): 
    pass
  def analysisTable(self): 
    pass
  def splitData(self): 
    pass

    