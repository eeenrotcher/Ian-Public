import yfinance as yf
import pandas as pd

#enter the date of a stock purchase in end date and the day before as start date
start_date = '2024-01-11'
end_date = '2024-01-13'

#enter your variables below
shares = 100
symbol = 'MFEIX'
stock = yf.Ticker(symbol)

#fetching the data and pulling adjusted closed from the end date
data = yf.download(symbol, start=start_date, end=end_date, auto_adjust=False)
adjusted_close = data['Adj Close'].iloc[-1]

print(f'{shares} shares of {symbol} on {end_date} have a cost basis of {adjusted_close * shares} at a price of {adjusted_close} per share.')

