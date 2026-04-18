import pandas as pd

df = pd.read_csv('employees.csv')

print(df['name'].tolist())
print(df[df['department'] == 'IT']['name'].tolist())
print(df['salary'].mean())
print(df.loc[df['salary'].idxmax(), 'name'])
print(df['department'].value_counts().to_dict())