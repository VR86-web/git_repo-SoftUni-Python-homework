data = input().split(" ")
stock = {}
for index in range(0, len(data), 2):
    food = data[index]
    quantity = int(data[index + 1])
    stock[food] = quantity
searched_products = input().split()
for current_product in searched_products:
    if current_product in stock:
        print(f"We have {stock[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")