import requests
import pandas as pd
from tabulate import tabulate

#Data extraction
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

#data transformation
df = pd.DataFrame(data)
df['title_length'] = df['title'].apply(len)

#Data load
csv_filepath = 'data.csv'
df.to_csv(csv_filepath, index= False)

#Data anaylsis
df_from_csv = pd.read_csv(csv_filepath)

#load data from the csv file
#display the entire data in a tavle format
print(tabulate(df_from_csv, headers='keys', tablefmt='pretty'))

#find average of title length
average_title_length = df_from_csv['title_length'].mean()

print(f'\n The average title length is :{average_title_length}')