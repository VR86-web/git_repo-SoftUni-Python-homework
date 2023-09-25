budget = int(input())
season = input()
num_of_fisherman = int(input())

price_of_rent_a_boat = 0

if season == "Spring":
    price_of_rent_a_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_of_rent_a_boat = 4200
elif season == "Winter":
    price_of_rent_a_boat = 2600
if num_of_fisherman <= 6:
    price_of_rent_a_boat *= 0.9
elif num_of_fisherman <= 11:
    price_of_rent_a_boat *= 0.85
else:
    price_of_rent_a_boat *= 0.75
if num_of_fisherman % 2 == 0 and season != "Autumn":
    price_of_rent_a_boat *= 0.95
money_left = abs(budget - price_of_rent_a_boat)
if budget >= price_of_rent_a_boat:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")


