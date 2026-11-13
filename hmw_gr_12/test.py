from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

housing = datasets.fetch_california_housing()

x = housing.data
y = housing.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 432)

print(housing.feature_names)
print(X_train[0], y_train[0])

