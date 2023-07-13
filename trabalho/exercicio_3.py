import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('Stores.csv', names=['Store ID', 'Store_Area', 'Items_Available', 'Store_Sales'])

ProfileReport(df, explorative=True)