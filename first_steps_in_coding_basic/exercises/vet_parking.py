number_of_days = int(input())
hours = int(input())
total_price = 0
for day in range(1, number_of_days + 1):
    parking_price = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_price += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            parking_price += 1.25
        else:
            parking_price += 1
    total_price += parking_price
    print(f"Day: {day} - {parking_price:.2f} leva")
print(f"Total: {total_price:.2f} leva")


