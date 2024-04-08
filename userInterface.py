import tkinter as tk
from tkinter import messagebox
import threading

class userInterface: 
  def __init__(self): 
    self.userSelectedStock = ""
    self.stockName = ""
    
  def initialiseUI(self): 
   root = tk.Tk()
   root.title("User Selects the Stock")
   
   #root will get updated this value for the string
   options = ["APPLE", "CHEVRON", "COCA COLA"] #create a drop down menu
   self.userSelectedStock = tk.StringVar(root)
   dropdown = tk.OptionMenu(root, self.userSelectedStock, *options)
   dropdown.pack(pady = 2)
    
   button = tk.Button(root, text= "Show Selected Option", command = self.whenSelected) #add the button
   button.pack(pady=10)
   self.stockMarketIdentifier()
   root.mainloop()
    
  def whenSelected(self): 
    userSelectedOption = self.userSelectedStock.get()
    self.stockMarketIdentifier()
    messagebox.showinfo("Selected Option", f"You selected: {userSelectedOption}")

  def stockMarketIdentifier(self):
    file = open("userSelectedStock.txt", "w")
    if self.userSelectedStock.get() == "APPLE": 
      self.stockName = "AAPL"
    elif self.userSelectedStock.get() == "CHEVRON": 
      self.stockName = "CVX"
    elif self.userSelectedStock.get() == "COCA COLA": 
      self.stockName = "KO"
    file.write(self.stockName)
    print(self.stockName, "self.stockName")
    file.close()
    
  def setUserSelectedStock(self, stock): 
    self.userSelectedStock = stock
  def getUserSelectedStock(self): 
    return self.userSelectedStock
  def setStockName(self, name): 
    self.stockName = name
  def getStockName(self): 
    print(self.stockName)
    return self.stockName
