number_of_kilometers = int(input())
time_of_the_day = input()
day_price = 0
night_price = 0
price = 0
if number_of_kilometers < 20:
    if time_of_the_day == "day":
        price = 0.79 * number_of_kilometers + 0.7
    elif time_of_the_day == "night":
        price = 0.9 * number_of_kilometers + 0.7
elif 20 <= number_of_kilometers < 100:
    price = 0.09 * number_of_kilometers
elif number_of_kilometers >= 100:
    price = 0.06 * number_of_kilometers
print(f"{price:.2f}")
