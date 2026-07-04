from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

X, y = make_regression(n_samples = 50, n_features=1, noise=40, random_state=88)

plt.scatter(X,y,s=70,c='g', edgecolor='k',alpha=0.6)
plt.grid()
plt.show()

print(X[0], y[0])

lr = LinearRegression()
lr.fit(X, y)
X_new = np.linspace(-2, 2.5, 100)
y_new = lr.predict(X_new.reshape(-1,1))
plt.scatter(X,y, s=70, c='g', edgecolor='k', alpha=0.5)
plt.plot(X_new, y_new, c='grey', ls='--')
plt.grid()
plt.show()

print(lr.coef_, lr.intercept_)

pre  = lr.predict([[3]])
pre

from sklearn.linear_model import Ridge
ridge = Ridge(alpha = 50)
ridge.fit(X,y)

y_new2 = ridge.predict(X_new.reshape(-1,1))
plt.scatter(X,y, s=70, c='g', edgecolor = 'k', alpha=0.6)
plt.plot(X_new, y_new, c='grey', ls='--', label = 'Linear Regression')
plt.plot(X_new, y_new2, c='k', ls=':', label='Ridge')
plt.grid()
plt.legend()
plt.show()

import jqdata
stocks = get_index_stocks('000016.XSHG')
q = query(valuation.code, valuation.market_cap, balance.total_assets-balance.total_liability, balance.total_assets/balance.total_liability, income.net_profit, indicator.inc_revenue_year_on_year, balance.development_expenditure).filter(valuation.code.in_(stocks))
df = get_fundamentals(q)
df.columns = ['code', 'mcap', 'na', '1/DA ratio','net income','growth','RD']
df.head()

df.index = df['code'].values
df = df.drop('code', axis=1)
X=df.drop('mcap', axis=1)
y = df['mcap']
X= X.fillna(0)
y = y.fillna(0)
reg = LinearRegression().fit(X,y)
predict = pd.DataFrame(reg.predict(X), index=y.index, columns=['predict_mcap'])
predict.head()

diff = df['mcap'] - predict['predict_mcap']
diff =  pd.DataFrame(diff, index = y.index, columns=['diff'])
diff = diff.sort_values(by = 'diff', ascending = True)
diff.head(10)
