days_of_stay = int(input())
type_of_room = input()
rating = input()

days_of_stay -= 1
price = 0

if type_of_room == "room for one person":
    price = 18
elif type_of_room == "apartment":
    price = 25
    if days_of_stay < 10:
        price *= 0.70
    elif days_of_stay <= 15:
        price *= 0.65
    elif days_of_stay > 15:
        price *= 0.5
elif type_of_room == "president apartment":
    price = 35
    if days_of_stay < 10:
        price *= 0.90
    elif days_of_stay <= 15:
        price *= 0.85
    elif days_of_stay > 15:
        price *= 0.8
total_price = days_of_stay * price
if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.9
print(f"{total_price:.2f}")

