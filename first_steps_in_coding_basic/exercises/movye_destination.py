movie_budget = float(input())
destination = input()
season = input()
num_of_days = int(input())
price = 0
if destination == "Dubai":
    if season == "Summer":
        price = 40000
    elif season == "Winter":
        price = 45000
elif destination == "Sofia":
    if season == "Summer":
        price = 12500
    elif season == "Winter":
        price = 17000
elif destination == "London":
    if season == "Summer":
        price = 20250
    elif season == "Winter":
        price = 24000
total_price = num_of_days * price
if destination == "Dubai":
    total_price = total_price * 0.7
if destination == "Sofia":
    total_price += total_price * 0.25
needed_money = abs(movie_budget - total_price)
if movie_budget >= total_price:
    print(f"The budget for the movie is enough! We have {needed_money:.2f} leva left!")
else:
    print(f"The director needs {needed_money:.2f} leva more!")