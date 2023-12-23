number_of_people = int(input())
season = input()
price = 0
if season == "spring":
    if number_of_people <= 5:
        price = 50
    elif number_of_people > 5:
        price = 48
elif season == "summer":
    if number_of_people <= 5:
        price = 48.5
    elif number_of_people > 5:
        price = 45
elif season == "autumn":
    if number_of_people <= 5:
        price = 60
    elif number_of_people > 5:
        price = 49.5
elif season ==  "winter":
    if number_of_people <= 5:
        price = 86
    elif number_of_people > 5:
        price = 85
total_price = price * number_of_people
if season == "summer":
    total_price -= total_price * 0.15
elif season == "winter":
    total_price += total_price * 0.08
print(f"{total_price:.2f} leva.")