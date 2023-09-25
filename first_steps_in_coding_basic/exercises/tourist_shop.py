budget = float(input())
product_name = input()
product_counter = 0
product_price_counter = 0
while product_name != "Stop":
    product_counter += 1
    product_price = float(input())
    if product_counter % 3 == 0:
        product_price = product_price / 2
    product_price_counter += product_price
    if product_price_counter > budget:
        money_needed = abs(product_price_counter - budget)
        print("You don't have enough money!")
        print(f"You need {money_needed:.2f} leva!")
        break
    product_name = input()
if product_name == "Stop":
    print(f"You bought {product_counter} products for {product_price_counter:.2f} leva.")