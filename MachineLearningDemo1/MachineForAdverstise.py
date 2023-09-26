# Python for Data Scientist: Quick Example

# Required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/scikit-learn-videos/master/data/Advertising.csv', index_col=0)
#print(data.head(150))
print(data)

# Simple visualization: Relationship between TV ads and Sales
plt.scatter(data['TV'], data['Sales'], color='blue', alpha=0.5)
plt.title('TV Ads vs Sales')
plt.xlabel('TV Advertisement Budget ($)')
plt.ylabel('Sales (in thousands)')
plt.show()

# Simple Linear Regression
X = data[['TV']]
y = data['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='True values')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predictions')
plt.title('Regression Line: TV Ads vs Sales')
plt.xlabel('TV Advertisement Budget ($)')
plt.ylabel('Sales (in thousands)')
plt.legend()
plt.show()
