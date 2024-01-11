budget = int(input())
total_price = 0
while True:
    product_price = input()
    if product_price == "End":
        print("You bought everything needed.")
        break
    current_product_price = int(product_price)
    if total_price + current_product_price > budget:
        print("You went in overdraft!")
        break
    total_price += current_product_price


