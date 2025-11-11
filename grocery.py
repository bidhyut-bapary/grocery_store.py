# Grocery Store Management System
# By: Bidhyut Bapary

print("===== Welcome to Grocery Store =====")

items = []  # পণ্যগুলোর লিস্ট
total = 0

while True:
    name = input("Enter product name: ")

    if name.lower() == 'done':
        break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    item_total = price * quantity
    items.append((name, price, quantity, item_total))
    total += item_total

print("\n===== BILL DETAILS =====")
print(f"{'Product':15} {'Price':10} {'Qty':5} {'Total':10}")
print("-" * 45)

for item in items:
    print(f"{item[0]:15} {item[1]:10.2f} {item[2]:5} {item[3]:10.2f}")

print("-" * 45)
print(f"Grand Total: {total:.2f} Tk")
print("===== Thank You! Visit Again =====")
