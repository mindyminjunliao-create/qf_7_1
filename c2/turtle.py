from pandas_datareader import data as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

start_date = '2020-01-01'
end_date = '2020-03-20'
zgpa = yf.download('601318.SS', start=start_date, end=end_date)
zgpa.columns = zgpa.columns.get_level_values(0)


#turtle trading
#generating transaction signal
turtle = pd.DataFrame(index = zgpa.index)
turtle['high'] = zgpa['Close'].shift(1).rolling(5).max()
turtle['low'] = zgpa['Close'].shift(1).rolling(5).min()
turtle['buy'] = zgpa['Close'] > turtle['high']
turtle['sell'] = zgpa['Close'] < turtle['low']
print(turtle.tail())

#transacting
turtle['orders']=0
positions=0
for k, (date, row) in enumerate(turtle.iterrows()):
    if row['buy'] and positions==0:
        turtle.loc[date, 'orders'] = 1
        positions = 1
    elif row['sell'] and positions > 0:
        turtle.loc[date, 'orders'] = -1
        positions = 0
#print(turtle.tail(15))

plt.figure(figsize=(10,5))
plt.plot(zgpa['Close'], lw=2)
plt.plot(turtle['high'], lw=2, ls='--', c='r')
plt.plot(turtle['low'], lw=2, ls='--', c='g')

plt.scatter(turtle.loc[turtle.orders==1].index, zgpa['Close'][turtle.orders==1], marker='^', s=80, c='r', label='Buy')
plt.scatter(turtle.loc[turtle.orders==-1].index, zgpa['Close'][turtle.orders==-1], marker='v', s=80, c='g', label='Sell')
plt.legend()
plt.grid()
plt.show()

#backtesting
initial_cash = 20000
positions = pd.DataFrame(index=turtle.index).fillna(0.0)
positions['stock'] = 100 * turtle['orders'].cumsum()
portfolio = positions.multiply(zgpa['Close'], axis=0)
portfolio['holding_values'] = (positions.multiply(zgpa['Close'], axis=0))
pos_diff = positions.diff()
portfolio['cash'] = initial_cash - (pos_diff.multiply(zgpa['Close'], axis=0)).cumsum()
portfolio['total'] = portfolio['cash'] + portfolio['holding_values']

plt.figure(figsize=(10,5))
plt.plot(portfolio['total'], label='total')
plt.plot(portfolio['holding_values'], '--', label='holding_values')
plt.grid()
plt.legend()
plt.show()
