collection_of_items = input().split("|")
budget = float(input())
items_new_price = []
bought_products = []
for collection in collection_of_items:
    current_collection = collection.split("->")
    items = current_collection[0]
    price = float(current_collection[1])
    buy_it = False
    if items == "Clothes":
        if 0 <= price <= 50:
            buy_it = True
    if items == "Shoes":
        if 0 <= price <= 35:
            buy_it = True
    if items == "Accessories":
        if 0 <= price <= 20.5:
            buy_it = True
    if budget < price:
        continue
    if buy_it:
        budget -= price
        bought_products.append(price)
        items_new_price.append(price * 1.4)
for price in items_new_price:
    print(f"{price:.2f}", end=" ")
print()
profit = sum(items_new_price) - sum(bought_products)
print(f"Profit: {profit:.2f}")
new_budget = budget + sum(items_new_price)
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
