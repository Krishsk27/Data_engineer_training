import pandas as pd

df = pd.read_csv('sales.csv')
df['revenue'] = df['quantity'] * df['price']
summary = df.groupby('product').agg({'quantity': 'sum', 'revenue': 'sum'})

print("Product Sales Summary")
for product, row in summary.iterrows():
    print(f"{product} → Qty: {row['quantity']} Revenue: {row['revenue']}")