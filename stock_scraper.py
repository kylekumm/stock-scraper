import yfinance as yf
from yfinance import ticker
import time, datetime
import excel_scraper as ex
from StockData import StockData

def printBasicInfo(ticker):
    longName = ticker.info["longName"]    
    #dateToday = datetime.date.today()
    print("Name: ",longName)
    print("Market Cap: ", ticker.info["marketCap"],ticker.info["currency"])

def printFiveDayHistory(ticker,shortName):
    print(shortName,"5 Day Trading History")
    print()    
    print(ticker.history(period="5d"))
    print()    

def printGainLossCalculations(ticker):
    # Previous Close
    previousClose = ticker.info["previousClose"]
    print("Previous Close: ",previousClose)

    # Todays Open
    todaysOpen = ticker.history(period="1d")["Open"][0]
    print("Todays Open: ",todaysOpen)

    # Todays Close
    todaysClose = ticker.history(period="1d")["Close"][0]
    print("Todays Close: ",todaysClose)    

    # % Gain/Loss Today (Yahoo Calculation)
    percentageGain = ((todaysClose - previousClose)/previousClose) * 100
    print("Gain/Loss:", round(percentageGain,2),"%")
    print()

stocks = ex.read_tickers()

#stocks = ["STXWDM.JO","STXNDQ.JO","SYGP.JO","AEG.JO","PPE.JO"] // Old method

startTime = time.time()

for i in range(0,len(stocks)): 
    shortName = stocks[i]
    #ticker = yf.Ticker(shortName)
    
    # Basic Stock Info
    #printBasicInfo(ticker)
    
    # 5 Day Trading History
    #printFiveDayHistory(ticker,shortName)

    # Gain/Loss Calculations
    #printGainLossCalculations(ticker)    

    # Create object to send to excel
    stockData = StockData(shortName)
    stockData.printData()
    ex.write_data(stockData)

endTime = time.time()
print("Execution time: ", endTime - startTime)
input()




