import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

response = requests.get(url)
response.raise_for_status()  # Raises an error if the request failed

csv_data = StringIO(response.text)

df = pd.read_csv(csv_data)

print(df.head())