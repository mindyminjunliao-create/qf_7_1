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


