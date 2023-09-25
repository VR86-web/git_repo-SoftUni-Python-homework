from math import floor, ceil

number_of_days = int(input())
available_food = float(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())
turtle_needed_food_per_day = turtle_food_per_day / 1000
total_needed_animal_food = dog_food_per_day * number_of_days \
                           + cat_food_per_day * number_of_days \
                           + turtle_needed_food_per_day * number_of_days

different = abs(available_food - total_needed_animal_food)
if available_food >= total_needed_animal_food:
    print(f"{floor(different)} kilos of food left.")
else:
    print(f"{ceil(different)} more kilos of food are needed.")
