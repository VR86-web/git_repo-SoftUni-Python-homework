budget = float(input())
number_of_series = int(input())
price_counter = 0
for series in range(number_of_series):
    name_of_series = input()
    price = float(input())
    if name_of_series == "Thrones":
        price -= price * 0.5
    elif name_of_series == "Lucifer":
        price -= price * 0.4
    elif name_of_series == "Protector":
        price -= price * 0.3
    elif name_of_series == "TotalDrama":
        price -= price * 0.2
    elif name_of_series == "Area":
        price -= price * 0.1
    price_counter += price
needed_money = abs(price_counter - budget)
if budget >= price_counter:
    print(f"You bought all the series and left with {needed_money:.2f} lv.")
else:
    print(f"You need {needed_money:.2f} lv. more to buy the series!")