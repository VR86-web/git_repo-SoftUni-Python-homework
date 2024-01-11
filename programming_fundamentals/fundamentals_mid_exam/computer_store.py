command = input()
sum_price = 0
while True:
    if command == "special" or command == "regular":
        break
    prices_without_tax = float(command)
    if prices_without_tax < 0:
        print("Invalid price!")
    else:
        sum_price += prices_without_tax
    command = input()
taxes = sum_price * 0.2
total_sum = sum_price + taxes
if command == "special":
    total_sum *= 0.9
if sum_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("----------- ")
    print(f"Total price: {total_sum:.2f}$")

