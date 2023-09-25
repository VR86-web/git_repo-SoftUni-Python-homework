number_of_clients = int(input())
total_price = 0
for clients in range(number_of_clients):
    command = input()
    items_counter = 0
    price_counter = 0
    while True:
        if command == "Finish":
            print(f"You purchased {items_counter} items for {price_counter:.2f} leva.")
            break
    if command == "basket":
        price_counter += 1.5
        items_counter += 1
    elif command == "wreath":
        price_counter += 3.8
        items_counter += 1
    elif command == "chocolate bunny":
        price_counter += 7
        items_counter += 1
    command = input()
    if items_counter % 2 == 0:
        price_counter = price_counter * 0.8
    total_price += price_counter
average_price = total_price / number_of_clients
print(f"Average bill per client is: {average_price:.2f} leva.")
