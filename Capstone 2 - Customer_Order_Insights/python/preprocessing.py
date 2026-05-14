import pandas as pd
import numpy as np

df = pd.read_csv("orders.csv")

df['delivery_date'] = pd.to_datetime(df['delivery_date'])

today = pd.Timestamp.today()

df['delay_days'] = (
    today - df['delivery_date']
).dt.days

df['delayed'] = np.where(
    df['delay_days'] > 0,
    1,
    0
)

top_delayed = df.groupby(
    'customer_id'
)['delayed'].sum().sort_values(
    ascending=False
)

common_issues = df['issue'].value_counts()

print(df)

print(top_delayed)

print(common_issues)

df.to_csv(
    "processed_orders.csv",
    index=False
)