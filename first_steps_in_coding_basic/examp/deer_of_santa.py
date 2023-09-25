from math import floor, ceil

num_of_days_santa_missing = int(input())
food_in_kilograms = int(input())
food_per_day_for_first_deer = float(input())
food_per_day_for_second_deer = float(input())
food_per_day_for_third_deer = float(input())

total_food_for_first_deer = num_of_days_santa_missing * food_per_day_for_first_deer
total_food_for_second_deer = num_of_days_santa_missing * food_per_day_for_second_deer
total_food_for_third_deer = num_of_days_santa_missing * food_per_day_for_third_deer
needed_food = total_food_for_first_deer + total_food_for_second_deer + total_food_for_third_deer
difference = abs(needed_food - food_in_kilograms)
if needed_food < food_in_kilograms:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")