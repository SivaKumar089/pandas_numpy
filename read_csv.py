import pandas as pd
pd.options.display.max_rows = 9999
data=pd.read_csv('data.csv')

# print(data)

# print(pd.options.display.max_rows) 

print(data.head())
print(data.tail())
print(data.info())