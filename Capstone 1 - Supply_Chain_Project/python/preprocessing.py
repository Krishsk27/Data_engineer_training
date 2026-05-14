import pandas as pd
import numpy as np

orders_df = pd.read_csv("../data/orders.csv")
inventory_df = pd.read_csv("../data/inventory.csv")
suppliers_df = pd.read_csv("../data/suppliers.csv")

orders_df['delivery_date'] = pd.to_datetime(orders_df['delivery_date'])

today = pd.Timestamp.today()

orders_df['delay_days'] = (
    today - orders_df['delivery_date']
).dt.days

orders_df['is_delayed'] = np.where(
    orders_df['delay_days'] > 0,
    1,
    0
)

low_stock_df = inventory_df[
    inventory_df['stock_quantity'] <
    inventory_df['reorder_level']
]

merged_df = orders_df.merge(
    suppliers_df,
    on='supplier_id',
    how='left'
)

print(merged_df)

print(low_stock_df)

merged_df.to_csv(
    "../data/processed_orders.csv",
    index=False
)

low_stock_df.to_csv(
    "../data/low_stock_inventory.csv",
    index=False
)