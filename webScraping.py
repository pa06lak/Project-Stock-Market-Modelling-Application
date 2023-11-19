import csv
from io import StringIO

import requests

from dataHandling import dataHandling
from replit import db 

class webScraping: 
  def __init__(self, URL, dataTempStorage, nameOfStock, Date): 
    self.URL = URL
    self.dataTempStorage = dataTempStorage
    self.nameOfStock = nameOfStock
    self.Date = Date
    self.data = []
    
  def dataRetrieval(self):
    
    # Retrieves data from the URL through web-scraping
    # Retrieves the HTML content of the page
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    stock_url = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1668192458&period2=1699728458&interval=1d&events=history'
    
    #this is an API call to get the data
    response = requests.get(stock_url, headers = headers)
    
    #splitting the query parameters -> more generalised and get better time stamps
    stock_url = "https://query1.finance.yahoo.com/v7/finance/download/{}?"
    stock = "AAPL"
    params = {
    "range" :'1y',
    "interval" : "1wk",
    "events" : "history"
    }
    response = requests.get(stock_url.format(stock), params= params, headers = headers )
    
    # Store the data
    file = StringIO(response.text)  # Creating a StringIO object
    reader = csv.reader(file)  # Creating a csv reader object to read from file
    data = list(reader)
    file = open("webScrape.txt", "w")
    file.write(stock + "\n")
    for row in data: 
      file.write(str(row) + "\n")
      #print(row)
    self.dataHandling() 
  
  def dataHandling(self): 
    #dataHandling(False, None, False, False, None, None)
    pass




#Do I need a main class?