import csv
from io import StringIO

import requests

from dataHandling import dataHandling
from replit import db 

class webScraping: 
  def __init__(self, nameOfStock): 
    self.stock = nameOfStock
    
  def dataRetrieval(self):
    
    # Retrieves data from the URL through web-scraping
    # Retrieves the HTML content of the page
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    makeURL = 'https://query1.finance.yahoo.com/v7/finance/download/' + str(self.getStock()) + '?period1=1668192458&period2=1699728458&interval=1d&events=history'
    stock_url = makeURL
    
    #this is an API call to get the data
    response = requests.get(stock_url, headers = headers)
    
    #splitting the query parameters -> more generalised and get better time stamps
    stock_url = "https://query1.finance.yahoo.com/v7/finance/download/{}?"
    stock = str(self.stock)
    params = {
    "range" :'6mo',
    "interval" : "1d",
    "events" : "history"
    }
    response = requests.get(stock_url.format(stock), params= params, headers = headers )
    
    # Store the data
    file = StringIO(response.text)  # Creating a StringIO object
    reader = csv.reader(file)  # Creating a csv reader object to read from file
    data = list(reader)
    file = open("webScrape.txt", "w")
    file.write(stock + "\n") #write the first line
    for row in data: #write each row from the stocks I have taken
      file.write(str(row) + "\n")
  def getStock(self): 
    return self.stock

