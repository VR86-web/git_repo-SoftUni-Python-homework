percent_of_fats = int(input())
percent_of_proteins = int(input())
percent_of_carbs = int(input())
number_of_calories = int(input())
percent_of_water = int(input())

total_grams_of_fats = (percent_of_fats * number_of_calories / 100) / 9
total_grams_of_protein = (percent_of_proteins * number_of_calories / 100) / 4
total_grams_carbs = (percent_of_carbs * number_of_calories / 100) / 4
total_weight_of_food = total_grams_of_fats + total_grams_of_protein + total_grams_carbs
calories_per_gram_food = number_of_calories / total_weight_of_food
weight_of_food_without_water = percent_of_water - 100
total_calories_per_gram_food = abs(weight_of_food_without_water * calories_per_gram_food / 100)

print(f"{total_calories_per_gram_food:.4f}")