needed_profit = float(input())
cocktail_price_counter = 0

party_is_over = False

while cocktail_price_counter < needed_profit:
    cocktail_name = input()
    if cocktail_name == "Party!":
        party_is_over = True
        break
    cocktail_order = input()
    if cocktail_order != "Party!":
        cocktail_order = int(cocktail_order)
    else:
        party_is_over = True
        break
    if int(len(cocktail_name)) * cocktail_order % 2 != 0:
        cocktail_price_counter += int(len(cocktail_name)) * cocktail_order * 0.75
    else:
        cocktail_price_counter += int(len(cocktail_name)) * cocktail_order
if party_is_over:
    difference = abs(needed_profit - cocktail_price_counter)
    print(f"We need {difference:.2f} leva more.")
elif cocktail_price_counter >= needed_profit:
    print("Target acquired.")
print(f"Club income - {cocktail_price_counter:.2f} leva.")