movie_budget = float(input())
num_of_statists = int(input())
price_per_clothing_of_one_statist = float(input())

price_per_decor = movie_budget * 0.10
total_price_of_clothing = num_of_statists * price_per_clothing_of_one_statist
if num_of_statists > 150:
    total_price_of_clothing -= total_price_of_clothing * 0.1
expenses = price_per_decor + total_price_of_clothing
difference = abs(movie_budget - expenses)

if expenses > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")