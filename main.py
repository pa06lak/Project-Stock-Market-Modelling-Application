from mainClass import Main
from database import Database
from datetime import *
import pickle

def getLastExecutionTime(): #get the date that this program was executed
  try:
      with open('last_execution_time.pickle', 'rb') as file:
          last_execution_time = pickle.load(file)
  except FileNotFoundError:
      last_execution_time = datetime.min
  return last_execution_time

def setLastExecutionTime(lastExecution): #sets the date for the program to be executed
  file = open("lastExecution.pickle", wb)
  pickle.dump(lastExecution, file)
  file.close()

def main(): 
  #stockArray = ["AAPL", "CVX", "KO"]
  stockArray = ["KO"]
  lastExecutionTime = getLastExecutionTime()
  currentTime = date.today()
  if currentTime != lastExecutionTime: #compare the date that the program was last executed
    for stock in stockArray: #for each stock I will get the data
      executeDaily(stock)
    setLastExecutionTime(currentTime)
  else: 
    stock = "KO"
    Main(stock).getGraph()
    
def executeDaily(stock): 
  Main(stock).dataRetrieval()
  print("main works")
  Length = Database(stock).createDatabase()
  print("database works")
  Arrays = Main(stock).dataHandling(Length)
  print("data handling works")
  predictionValue = Main(stock).trainModel(Arrays)
  print("machine learning works")
  Main(stock).generatePredictions(predictionValue)
  print("Finished")
  exit()

if __name__ == "__main__": 
  main()
