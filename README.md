# stock-scraper
Small python script that checks data of certain JSE listed stocks or ETFs and exports the data to an excel sheet. I created this in 2021 after learning some Python basics in my CMPG111 class, and wanted to create something rudimentary to test myself and simultaneously try something new. It was made with the intention that I get to have instantaneous access to the data as well as be able to do my own analysis offline.

Solving the Problem

I wanted an easy way to be able to input the required ticker symbols to be accessed, and decided to go with Excel, as we would also be exporting to Excel and it would be asier for someone to be able to input data to Excel than edit a file using Notepad or similar. The excel_scraper is used to read and write to and from seperate Excel files.
The main script file is the stock_scraper.py file which reads in the tickers and starts a timer. The data is then acquired from the StockData.py file (an object which gets the info from the yfinance API wrapper and returns it) and writes it to the console, as well as an Excel file. When the process is completed the timer stops and the execution time is displayed as well as info on the stocks.

Some Notes

I haven't worked on this in almost 2 years, but some future changes could include:
- A GUI or web interface to add, update or remove tickers instead of using an Excel file
- Storing the data in a database such as mySQL or similar.
- A GUI or web interface for displaying data and potentially charting the data as well.
