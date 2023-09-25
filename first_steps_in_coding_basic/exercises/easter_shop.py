quantity_eggs_in_shop = int(input())
command = input()
buy_eggs_counter = 0
while command != "Close":
    eggs_counter = int(input())
    if command == "Buy":
        if eggs_counter > quantity_eggs_in_shop:
            print("Not enough eggs in store!")
            print(f"You can buy only {quantity_eggs_in_shop}.")
            break
        quantity_eggs_in_shop -= eggs_counter
        buy_eggs_counter += eggs_counter
    elif command == "Fill":
        quantity_eggs_in_shop += eggs_counter
    command = input()
if command == "Close":
    print("Store is closed!")
    print(f"{buy_eggs_counter} eggs sold.")

