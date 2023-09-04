# Required Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import MinMaxScaler

# Data Collection
data = {
    'Size': [1500, 2500, 1200, 1800, 2200, 3000],
    'Bedrooms': [3, 4, 2, 4, 3, 5],
    'Location_Score': [7, 8, 5, 7, 7, 9],
    'Price': [300000, 500000, 220000, 330000, 350000, 650000]
}

df = pd.DataFrame(data)
print("Dataframe:\n", df)

# Feature Selection & Scaling
X = df[['Size', 'Bedrooms', 'Location_Score']]
y = df['Price']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Model Selection & Cross-Validation for Linear Regression
model = LinearRegression()
scores = cross_val_score(model, X_scaled, y, cv=5, scoring='neg_mean_absolute_error')
print("\nLinear Regression - MAE for each fold:", -scores)
print("Linear Regression - Average MAE across folds:", np.mean(-scores))

# Model Selection & Cross-Validation for Ridge Regression
ridge_model = Ridge(alpha=1.0)
ridge_scores = cross_val_score(ridge_model, X_scaled, y, cv=5, scoring='neg_mean_absolute_error')
print("\nRidge Regression - MAE for each fold:", -ridge_scores)
print("Ridge Regression - Average MAE across folds:", np.mean(-ridge_scores))
