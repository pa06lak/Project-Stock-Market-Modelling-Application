import tkinter as tk
from tkinter import messagebox
import threading

class userInterface: 
  def __init__(self): 
    self.userSelectedStock = ""
    self.stockName = " "
    
  def initialiseUI(self): 
   root = tk.Tk()
   root.title("User Selects the Stock")
   stock = tk.StringVar(root)
   self.setUserSelectedStock(stock)
   #root will get updated this value for the string
   options = ["APPLE", "CHEVRON", "COCA COLA"] #create a drop down menu
   dropdown = tk.OptionMenu(root, self.getUserSelectedStock(), *options)
   dropdown.pack(pady = 2)
    
   button = tk.Button(root, text= "Show Selected Option", command = self.whenSelected) #add the button
   button.pack(pady=10)
   self.stockMarketIdentifier()
   #return self.stockName
   return 
   root.mainloop()
    
  def whenSelected(self): 
    userSelectedOption = self.userSelectedStock.get()
    print(userSelectedOption)
    messagebox.showinfo("Selected Option", f"You selected: {userSelectedOption}")

  def stockMarketIdentifier(self):
    print(self.userSelectedStock.get(), "this is the user stock")
    if self.getUserSelectedStock() == "APPLE": 
      self.stockName = "AAPL"
    elif self.getUserSelectedStock() == "CHEVRON": 
      self.stockName = "CVX"
    elif self.getUserSelectedStock() == "COCA COLA": 
      self.stockName = "KO"
    
  def displayChart(self): 
    pass
  def showPredictions(self): 
    pass
    
  def setUserSelectedStock(self, stock): 
    self.userSelectedStock = stock
  def getUserSelectedStock(self): 
    return self.userSelectedStock
  def setStockName(self, name): 
    self.stockName = name
  def getStockName(self): 
    print("soemthing")
    print(self.stockName)
    return self.stockName
