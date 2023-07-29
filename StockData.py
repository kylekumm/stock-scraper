import datetime
import yfinance as yf
from yfinance import ticker

class StockData:
    def __init__(self,short):
        self.shortName = short
        self.ticker = yf.Ticker(self.shortName)
        self.set_name()
        self.set_prices()                        

    def set_name(self):
        self.longName = self.ticker.info["longName"]

    def set_prices(self):
        self.previousClose = self.ticker.info["previousClose"]
        self.todayOpen = self.ticker.history(period="1d")["Open"][0]
        self.todayClose = self.ticker.history(period="1d")["Close"][0]

    def get_date(self):
        dateToday = datetime.date.today()
        return dateToday

    def get_percentageGain(self):
        gain = ((self.todayClose - self.previousClose)/self.previousClose) * 100 
        return round(gain,2)

    def printData(self):
        print("Name: ", self.longName)
        print("Ticker: ",self.shortName)
        print("Date: ",self.get_date())
        print("Previous Close: ",self.previousClose)
        print("Todays Open: ", self.todayOpen)
        print("Todays Close: ",self.todayClose)
        print("Percentage Gain: ",self.get_percentageGain(),"%")
        print()
