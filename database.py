from replit import db

class Database: 
  def __init__(self, nameOfStock): 
    self.nameOfStock = nameOfStock


  
  def createDatabase(self): 
    tempStore = [] #temp list storage for the row 
    file = open("webScrape.txt", "r")
    counter = 0
    for row in file: 
      rowList = row.strip().split(',')
      tempStore.append(rowList)
      date = tempStore[counter][0]
      #print(date)
      counter = counter + 1

  
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






#here I want to create multiple databases for multiple stocks or should I have multiple tables so one per stock
#or should I web-scrape whenever I need and keep on going through the processes

    