from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

X, y = data.data, data.target
X_train, X_test, y_train, y_test =\
        train_test_split(X, y)

knn_reg = KNeighborsRegressor()
knn_reg.fit(X_train, y_train)
print('train set accuracy: %.2f'%knn_reg.score(X_train, y_train))
print('test set accuracy: %.2f'%knn_reg.score(X_test, y_test))

