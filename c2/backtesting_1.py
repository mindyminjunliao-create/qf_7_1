from pandas_datareader import data as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

start_date = '2020-01-01'
end_date = '2020-03-20'
zgpa = yf.download('601318.SS', start=start_date, end=end_date)
#print(zgpa.head())

zgpa_signal = pd.DataFrame(index = zgpa.index)
zgpa_signal['price'] = zgpa['Close']
zgpa_signal['diff'] = zgpa_signal['price'].diff()
zgpa_signal = zgpa_signal.fillna(0.0)
zgpa_signal['signal'] = np.where(zgpa_signal['diff'] >= 0, 0, 1)
zgpa_signal['order'] = zgpa_signal['signal'].diff()*100
#print(zgpa_signal.head())

initial_cash = 20000.00
zgpa_signal['stock'] = zgpa_signal['order']*zgpa_signal['price']
zgpa_signal['cash'] = initial_cash -\
        (zgpa_signal['order'].diff()*zgpa_signal['price']).cumsum()
zgpa_signal['total'] = zgpa_signal['stock'] + zgpa_signal['cash']

plt.figure(figsize=(10,6))
plt.plot(zgpa_signal['total'])
plt.plot(zgpa_signal['order'].cumsum()*zgpa_signal['price'], '--', label = 'stocke value')
plt.grid()
plt.legend(loc='center right')
#plt.show()

#单一平均移动指标
period = 10
avg_10 = []
avg_value = []
for price in zgpa['Close'].squeeze():
    avg_10.append(price)
    if len(avg_10) > period:
          del avg_10[0]
    avg_value.append(np.mean(avg_10))
zgpa = zgpa.assign(avg_10 = pd.Series(avg_value, index = zgpa.index))
#print(zgpa.head())
 
plt.figure(figsize=(10,6))
plt.plot(zgpa['Close'], lw=2, c='k', label='stock price')
plt.plot(zgpa['avg_10'], '--', lw=2, c='b', label='10_avg')
plt.legend()
plt.grid()
plt.show()
