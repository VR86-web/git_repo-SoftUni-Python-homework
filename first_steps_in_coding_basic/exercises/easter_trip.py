import datetime

destination = input()
date_of_reservation = input()
number_of_nights = int(input())
price = 0
if destination == "France":
    if date_of_reservation == 21-23:
        price = 30
    elif date_of_reservation == 24-27:
        price = 35
    elif date_of_reservation == 28-31:
        price = 40
elif destination == "Italy":
    if date_of_reservation == 21-23:
        price = 28
    elif date_of_reservation == 24-27:
        price = 32
    elif date_of_reservation == 28-31:
        price = 39
elif destination == "Germany":
    if date_of_reservation == 21-23:
        price = 32
    elif date_of_reservation == 24-27:
        price = 37
    elif date_of_reservation == 28-31:
        price = 43
total_price = number_of_nights * price
print(f"Easter trip to {destination} : {total_price:.2f} leva.")