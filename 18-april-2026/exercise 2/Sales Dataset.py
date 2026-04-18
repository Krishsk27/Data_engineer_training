import pandas as pd

df = pd.read_csv('sales.csv')
df['total'] = df['quantity'] * df['price']

print(df['total'].sum())
print(df.groupby('product')['quantity'].sum().to_dict())


rev = df.groupby('product')['total'].sum()
print(rev.idxmax())
print(rev.to_dict())
print(rev[rev > 50000].index.tolist())