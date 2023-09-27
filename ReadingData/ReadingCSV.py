import pandas as pd
# Read CSV file
data = pd.read_csv('data.csv')
# Display first 5 rows (Original Data)
print("Original Data:")
print(data.head())

# 1. Add a full name column
data['fullname'] = data['firstname'] + " " + data['lastname']

# 2. Filter rows where age is less than 30
data = data[data['age'] < 30]

# 3. Sort by age in descending order
data = data.sort_values(by='age', ascending=False)

# Display first 5 rows (Manipulated Data)
print("\nManipulated Data:")
print(data.head())

# Save the manipulated data to output.csv
data.to_csv('output.csv', index=False)
