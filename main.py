from mainClass import Main
from database import Database
from datetime import date
from datetime import *
import pickle
import sys
import tkinter as tk
from tkinter import messagebox
import threading

def getLastExecutionTime(): #get the date that this program was executed
  file = open("lastExecution.txt", "r")
  lastExecuted = file.read()
  file.close()
  return lastExecuted

def setLastExecutionTime(lastExecution): #sets the date for the program to be executed
  file = open("lastExecution.txt", "w")
  formattedDateTime = lastExecution.strftime('%Y-%m-%d')      
  file.write(formattedDateTime)
  file.close()
  
def main(): 
  stockArray = ["CVX", "KO"]
  lastExecutionTime = getLastExecutionTime()
  print(lastExecutionTime, "last time this was executed")
  currentTime = date.today()
  if str(currentTime) != lastExecutionTime: #compare the date that the program was last executed
    for stock in stockArray: #for each stock I will get the data
      print("Something")
      print(stock)
      executeDaily(stock)
    setLastExecutionTime(lastExecutionTime)
  else: 
    gui_thread = threading.Thread(target=Main(None).startUserInterface())
    gui_thread.start()
    #UserStock = Main(None).getUserInputtedStock()
    #print(UserStock, "this is the user Stock")
    stock = "KO"
    Main(stock).getGraph()
  sys.exit()
    
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
  print("go to the end")

if __name__ == "__main__": 
  main()
