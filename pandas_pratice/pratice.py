import pandas as pd

df=pd.read_csv('Employees.csv')

print(df)
# print(df.loc[1])
# print(df.shape)
# print(df.shape[0])
# print(df.shape[1])
# print(df.columns)
# print(df.head())


# print(df.groupby('department').sum())
# print(df.groupby('department').count())
# print(df.groupby('department')['id'].count())
# print(df['age']>30)
# print(df[df['age']>30]['name'])
# print(df[df['department']=='IT']['name'])
# print(df[(df['age']>30) & ( 60000<= df['salary'])]['name'])
# print(df[['name','salary']])
# print(df[df['salary'] == df['salary'].max()]['name'])
# print(df['join_date'] = pd.to_datetime(df['join_date']))
# print(df.sort_values(by='join_date', ascending=True))
# print(df.sort_values(by='join_date', ascending=False))

# print(df.drop_duplicates(subset=['salary']))

# print(df.drop_duplicates(subset=['salary'])['name'])
# print(df[df.duplicated(subset=['salary'], keep=False)]['name'])
# df = df.drop_duplicates(subset=['salary'])


# print(df[df['age'] == df['age'].min()]['name'])
# print(df[df['age'] == df['age'].max()]['name'])
# print(df.loc[df['age'].idxmin(), 'name'])
# print(df.loc[df['age'].idxmax(), 'name'])
# print(df.loc[df['age'].idxmean(), 'name'])


# print(df.groupby('department')['id'].count())

# print(df.groupby('department')['salary'].sum())
# print(df.groupby('department')['salary'].mean())

# print(df.groupby('department')['salary'].mean().idxmax())

# print(df[pd.to_datetime(df['join_date']) <= (pd.Timestamp.today() - pd.DateOffset(years=5))]['name'])

# df['experience_years'] =(pd.Timestamp.today()- pd.to_datetime(df['join_date'])).dt.days // 365
# print(df)

# print(df.loc[df.groupby('department')['salary'].idxmax(),'name'])

# df.loc[df['name'] =='Daniel','salary']=75000

new_row = {
    "id": 9,
    "name": "Vikram",
    "age":28,
    "department": "IT",
    "salary": 80000,
    "join_date": "2023-01-01"
}

df = df._append(new_row, ignore_index=True)
# df = df[df['name'] != 'Vikram'] 

df.to_csv("Employees.csv", index=False)
print(df)