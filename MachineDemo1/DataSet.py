import pandas as pd
import numpy as np

#Set seed for reproducibility
np.random.seed(42)

#Generate 100000 data points
n_sample = 10000
# generate random house size between 1000 and 5000 sqft
sizes = np.random.randint(1000, 5000, n_sample)
#Genertae random house bedroom in between 1 and 5
bedrooms = np.random.randint(1,6,n_sample)
#Generate Random score location between 1 and 10
location_scores  = np.random.randint(1,11, n_sample)
# Generate house prices based on a hypothetical formula
# Price = base_price + price_per_sqft*size + price_per_bedroom*bedrooms + price_per_location_score*location_score + random_noise
base_price = 50000
price_per_sqft = 50
price_per_bedroom = 5000
price_per_location_score = 10000
random_noise = np.random.normal(0, 15000, n_sample)  # Some noise to make the data more realistic

prices = (base_price +
          price_per_sqft * sizes +
          price_per_bedroom * bedrooms +
          price_per_location_score * location_scores +
          random_noise).astype(int)

# Create a DataFrame
df = pd.DataFrame({
    'Size': sizes,
    'Bedrooms': bedrooms,
    'Location_Score': location_scores,
    'Price': prices
})
# Save the DataFrame to a CSV file
df.to_csv('house_data.csv', index=False)


