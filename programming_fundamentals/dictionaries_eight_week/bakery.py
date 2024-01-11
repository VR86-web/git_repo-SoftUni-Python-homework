data = input().split()

stock = {}

for product in range(0, len(data), 2):
    food = data[product]
    quantity = data[product + 1]
    stock[food] = int(quantity)
print(stock)
