
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#1 Data Collection
data = {
       'Size': [1500, 2500, 1200, 1800, 2200, 3000],
       'Bedrooms': [3, 4, 2, 4, 3, 5],
       'Location_Score': [7, 8, 5, 7, 7, 9],
       'Price': [300000, 500000, 220000, 330000, 350000, 650000]
}

# This will print the table for size bedroom location and price as heading and all other
# data as the columns
df = pd.DataFrame(data)
print("DataFrame\n", df)

#3 Feature Selection (Implicit in our data collection)
X = df[['Size', 'Bedrooms', 'Location_Score']]
y = df['Price']

#4 Training and Test Splits
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.2, random_state= 42)

#5 Model Selection
model = LinearRegression()

#6 Model Training
model.fit(X_train, y_train)

#7 Testing
predictions = model.predict(X_test)
print("\nPredictions: ", predictions)

#8 Evaluation
mae = mean_absolute_error(y_test, predictions)
print(f"\nMean Absolute Error: {mae}")

