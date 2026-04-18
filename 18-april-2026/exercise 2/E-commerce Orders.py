import json

with open('orders.json', 'r') as f:
    data = json.load(f)
    orders = data['orders']

print(orders)
print(sum(o['amount'] for o in orders))

spending = {}
counts = {}
for o in orders:
    spending[o['customer']] = spending.get(o['customer'], 0) + o['amount']
    counts[o['customer']] = counts.get(o['customer'], 0) + 1

print(spending)
print(max(spending, key=spending.get))
print(counts)