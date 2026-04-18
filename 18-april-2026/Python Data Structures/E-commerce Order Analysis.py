orders = [
    {"order_id": 1, "customer": "Rahul", "amount": 2500},
    {"order_id": 2, "customer": "Sneha", "amount": 1800},
    {"order_id": 3, "customer": "Rahul", "amount": 3200},
    {"order_id": 4, "customer": "Amit", "amount": 1500}
]

spending = {}
order_count = {}

for o in orders:
    cust = o["customer"]
    spending[cust] = spending.get(cust, 0) + o["amount"]
    order_count[cust] = order_count.get(cust, 0) + 1

highest_spender = max(spending, key=spending.get)

print(f"Total Spending: {spending}")
print(f"Highest Spender: {highest_spender}")
print(f"Orders per Customer: {order_count}")