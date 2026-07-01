import pandas_datareader as web
import yfinance as yf

start_date = '2020-01-01'
end_date = '2020-03-18'

data = yf.download('601318.SS', start = start_date, end=end_date)
print(data.head())
