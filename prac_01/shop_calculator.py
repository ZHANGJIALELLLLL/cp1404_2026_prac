"""
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""

items = int(input("Number of items:"))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items:"))
total = 0
for i in range(items):
    price = float(input("Price of item:"))
    total += price
if total > 100:
    total *= 0.9 #total > 100 折扣 10% 所以 total * 90%

print(f"Total price for {items} items is ${total:.2f}")



