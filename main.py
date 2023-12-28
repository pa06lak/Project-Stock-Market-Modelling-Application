from mainClass import Main
from database import Database

#Main("https://uk.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch", "dataTempStorage", "AAPL", "2021-06-02").dataRetrieval()
Length = Database(None).createDatabase()
Main("https://uk.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch", "dataTempStorage", "AAPL", "2021-06-02").dataHandling(Length)


