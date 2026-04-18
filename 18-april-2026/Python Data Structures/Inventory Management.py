inventory = {"laptop": 10, "mouse": 25, "keyboard": 15}

inventory["monitor"] = 8
inventory["laptop"] -= 2
low_stock = {item: stock for item, stock in inventory.items() if stock < 10}

print(f"Low stock items: {low_stock}")