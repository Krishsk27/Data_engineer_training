import pandas as pd

orders_df = pd.read_csv("../data/orders.csv")
inventory_df = pd.read_csv("../data/inventory.csv")
suppliers_df = pd.read_csv("../data/suppliers.csv")

print(orders_df.head())
print(inventory_df.head())
print(suppliers_df.head())