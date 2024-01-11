products_dict = {}
while True:
    data = input()
    if data == "buy":
        break
    products, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if products not in products_dict.keys():
        products_dict[products] = [price, quantity]
    else:
        products_dict[products][0] = price
        products_dict[products][1] += quantity
for name, value in products_dict.items():
    total_price = value[0] * value[1]
    print(f"{name} -> {total_price:.2f}")