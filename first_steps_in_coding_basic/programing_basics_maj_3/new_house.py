kind_of_flowers = input()
num_of_flowers = int(input())
budget = int(input())
price = 0

if kind_of_flowers == "Roses":
    price = 5
    if num_of_flowers > 80:
        price *= 0.9
elif kind_of_flowers == "Dahlias":
    price = 3.8
    if num_of_flowers > 90:
        price *= 0.85
elif kind_of_flowers == "Tulips":
    price = 2.8
    if num_of_flowers > 80:
        price *= 0.85
elif kind_of_flowers == "Narcissus":
    price = 3
    if num_of_flowers < 120:
        price *= 1.15
elif kind_of_flowers == "Gladiolus":
    price = 2.5
    if num_of_flowers < 80:
        price *= 1.2
total_price = price * num_of_flowers
money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {num_of_flowers} {kind_of_flowers} and {money_left:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {money_left:.2f} leva more.")