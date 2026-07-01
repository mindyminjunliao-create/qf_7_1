import pandas_datareader as web
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

start_date = '2020-01-01'
end_date = '2020-03-18'
data = yf.download('601318.SS', start = start_date, end=end_date)

data['diff'] = data['Close'].diff()
data['Signal'] = np.where(data['diff']>0, 1, 0)

plt.figure(figsize = (10,5))
data['Close'].plot(linewidth=2, color='k', grid=True)
plt.scatter(data['Close'].loc[data.Signal==1].index, data['Close'][data.Signal==1], marker = 'v', s=80, c='g')
plt.scatter(data['Close'].loc[data.Signal==0].index, data['Close'][data.Signal==0], marker = '^', s=80, c='r')
print(data.head())
plt.show()
