import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from class_random_forest import RandomForest

data = datasets.load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)


clf = RandomForest()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test, y_test)
acc = accuracy(y_test, predictions)
print(acc)