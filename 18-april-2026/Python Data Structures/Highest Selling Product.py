sales = [
    {"product": "Laptop", "qty": 5},
    {"product": "Mouse", "qty": 20},
    {"product": "Laptop", "qty": 3},
    {"product": "Keyboard", "qty": 10}
]

totals = {}
for entry in sales:
    p = entry["product"]
    totals[p] = totals.get(p, 0) + entry["qty"]

highest_product = max(totals, key=totals.get)
print(f"Total Sales: {totals}")
print(f"Highest Seller: {highest_product}")