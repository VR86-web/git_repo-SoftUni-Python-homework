month = input()
num_of_nights = int(input())
price_per_apartment = 0
price_per_studio = 0

if month == "May" or month == "October":
    price_per_apartment = 65
    price_per_studio = 50
    if 7 <= num_of_nights <= 14:
        price_per_studio *= 0.95
    elif num_of_nights > 14:
        price_per_studio *= 0.70
elif month == "June" or month == "September":
    price_per_apartment = 68.7
    price_per_studio = 75.2
    if num_of_nights > 14:
        price_per_studio *= 0.80
elif month == "July" or month == "August":
    price_per_apartment = 77
    price_per_studio = 76
if num_of_nights > 14:
    price_per_apartment *= 0.90
total_price_per_apartment = num_of_nights * price_per_apartment
total_price_per_studio = num_of_nights * price_per_studio


print(f"Apartment: {total_price_per_apartment:.2f} lv.")
print(f"Studio: {total_price_per_studio:.2f} lv.")
