from math import ceil

number_of_people = int(input())
entry_price = float(input())
price_per_sun_lounger = float(input())
price_per_umbrella = float(input())

people_witch_use_sun_lounger = ceil(number_of_people * 0.75)
people_witch_use_umbrella = ceil(number_of_people / 2)
total_money_for_entry = number_of_people * entry_price
needed_money_for_sun_loungers = people_witch_use_sun_lounger * price_per_sun_lounger
needed_money_for_umbrellas = people_witch_use_umbrella * price_per_umbrella

total_needed_money = total_money_for_entry + needed_money_for_umbrellas + needed_money_for_sun_loungers
print(f"{total_needed_money:.2f} lv.")