import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def load_stock(start_date, end_date, output_file):
    try:
        df = pd.read_pickle(output_file)
        if df.empty:
            raise FileNotFoundError
        print('finished loading the stock data file')

    except FileNotFoundError:
        print('文件未找到，重新下载中')
        df = yf.download('601318.SS', start=start_date, end=end_date)

        df.columns = df.columns.get_level_values(0)
        df.to_pickle(output_file)
        print('下载完成')

    return df


zgpa = load_stock(start_date = '2017-03-09', end_date = '2020-03-05', output_file = '601318.pkl')
print(zgpa.head())

#create transaction consition
def classification_tc(df):
    df['Open-Close']  = df['Open'] - df['Close']
    df['High-Low'] = df['High'] - df['Low']

    df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, -1)
    df = df.dropna()
    X = df[['Open-Close', 'High-Low']]
    y = df['target']

    return(X, y)

def regression_tc(df):
    df['Open-Close']  = df['Open'] - df['Close']
    df['High-Low'] = df['High'] - df['Low']

    df['target'] = df['Close'].shift(-1) - df['Close']
    df = df.dropna()
    X = df[['Open-Close', 'High-Low']]
    y = df['target']
    return(X, y)

#calculate basic gain
def cum_return(df, split_value):
    cum_return = df[split_value:]['Return'].cumsum()*100
    return cum_return

#calculate strategic gain
def strategy_return(df, split_value):
    df['Strategy Return'] = df['Return'] * df['Predict Signal'].shift(1)
    cum_strategy_return = df[split_value:]['Strategy Return'].cumsum()*100
    return cum_strategy_return

#plot
def plot_chart(cum_return, cum_strategy_return):
    plt.figure(figsize=(9,6))
    plt.plot(cum_return, '--', label = 'Returns')
    plt.plot(cum_strategy_return, label = 'Strategy Returns')
    plt.legend()
    plt.show()

#transaction strategy using classification
X, y = classification_tc(zgpa)
X_train, X_test, y_train, y_test = \
        train_test_split(X, y, train_size=0.8)
knn_clf = KNeighborsClassifier(n_neighbors=95)
knn_clf.fit(X_train, y_train)
print(knn_clf.score(X_train, y_train))
print(knn_clf.score(X_test, y_test))

zgpa['Predict Signal'] = knn_clf.predict(X)
zgpa['Return'] = np.log(zgpa['Close']/zgpa['Close'].shift(1))
print(zgpa.head())

#compare basic and strategic return
cum_return = cum_return(zgpa, split_value=len(X_train))
cum_strategy_return = strategy_return(zgpa, split_value=len(X_train))
plot_chart(cum_return, cum_strategy_return)
