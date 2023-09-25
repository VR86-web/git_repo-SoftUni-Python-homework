hot_drink = input()
sugar = input()
number_of_drinks = int(input())
price = 0
bill = 0
if hot_drink == "Espresso":
    price = 0.9
    if sugar == "Without":
        price = price * 0.65
    elif sugar == "Normal":
        price = 1.0
    elif sugar == "Extra":
        price = 1.2
    if number_of_drinks >= 5:
        price = price * 0.75
elif hot_drink == "Cappuccino":
    price = 1.0
    if sugar == "Without":
        price = price * 0.65
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif hot_drink == "Tea":
    price = 0.5
    if sugar == "Without":
        price = price * 0.65
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

total_price = number_of_drinks * price
if total_price > 15:
    total_price = total_price * 0.8
print(f"You bought {number_of_drinks} cups of {hot_drink} for {total_price:.2f} lv.")