from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test =\
        train_test_split(X, y)
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_train)
print('train set accuracy:%.2f'%knn_clf.score(X_train, y_train))
print('test set accuracy:%.2f'%knn_clf.score(X_test, y_test))

#寻找模型最优参数
n_neighbors= tuple(range(1, 11, 1))
cv = GridSearchCV(estimator=KNeighborsClassifier(), param_grid = {'n_neighbors':n_neighbors}, cv = 5)
cv.fit(X, y)
print(cv.best_params_)
