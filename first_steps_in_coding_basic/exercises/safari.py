budget = float(input())
liters_fuel_needed = float(input())
day_of_week = input()
price_per_liter_fuel = 2.1
guide_price = 100
total_cost = liters_fuel_needed * price_per_liter_fuel + guide_price
if day_of_week == "Saturday":
    total_cost -= total_cost * 0.1
elif day_of_week == "Sunday":
    total_cost -= total_cost * 0.2
needed_money = abs(total_cost - budget)
if budget >= total_cost:
    print(f"Safari time! Money left: {needed_money:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {needed_money:.2f} lv.")