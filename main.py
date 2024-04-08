from mainClass import Main
import datetime
from database import Database
from datetime import date
from datetime import *
import pickle
import sys
import tkinter as tk
from tkinter import messagebox
import threading
from replit import db

def getLastExecutionTime(): #get the date that this program was executed
  file = open("lastExecution.txt", "r")
  lastExecuted = file.read()
  file.close()
  return lastExecuted

def setLastExecutionTime(lastExecution): #sets the date for the program to be executed
  file = open("lastExecution.txt", "w")
  file.write(lastExecution)
  file.close()

def isWeekend():
  today = datetime.today().weekday()
  return today == 4#return True if today is 5 or 6
  
def main(): 
  stockArray = ["AAPL", "CVX", "KO"]
  lastExecutionTime = getLastExecutionTime()
  weekend = isWeekend()
  print(lastExecutionTime, "last time this was executed")
  currentTime = datetime.now()
  currentTime = currentTime.strftime("%m/%d/%Y")
  print(currentTime)
  if str(currentTime) != lastExecutionTime: #compare the 
    #date that the program was last executed 
    # & if it is a weekend
    for stock in stockArray: #for each stock I will get the data
      print("Something")
      print(stock)
      executeDaily(stock)
    setLastExecutionTime(lastExecutionTime)
  else: 
    try:
      gui_thread = threading.Thread(target=Main(None).startUserInterface)
      gui_thread.start()
      with open("userSelectedStock.txt", "r") as file:
          stock = file.read()
          print(stock, "this is the name")
      Main(stock).getGraph()
    except Exception as e:
      print("An error occurred:", e)
      with open("userSelectedStock.txt", "r") as file:
        stock = file.read()
        print(stock, "this is the name")
    finally:
      sys.exit()
    
def executeDaily(stock): 
  Main(stock).dataRetrieval()
  print("main works")
  Length = Database(stock).createDatabase()
  print("database works")
  #differences = Main(stock).getDifferences()
  #print("differences work")
  Arrays = Main(stock).dataHandling(Length)
  print("data handling works")
  predictionValue = Main(stock).trainModel(Arrays)
  print("machine learning works")
  Main(stock).generatePredicitons(predictionValue)
  print("Finished")
  print("go to the end")

if __name__ == "__main__": 
  print(isWeekend())
  main()
  now = datetime.now()
  dateTime = now.strftime("%m/%d/%Y")
  setLastExecutionTime(dateTime)