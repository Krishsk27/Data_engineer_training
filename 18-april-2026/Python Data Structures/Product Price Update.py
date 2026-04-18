products = {"Laptop": 75000, "Mobile": 30000, "Tablet": 25000}

products = {k: v * 1.10 for k, v in products.items()}
print(f"Updated Prices: {products}")