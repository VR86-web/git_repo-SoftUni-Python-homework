number_of_painted_eggs = int(input())
red_eggs_counter = 0
orange_eggs_counter = 0
blue_eggs_counter = 0
green_eggs_counter = 0
for eggs in range(number_of_painted_eggs):
    egg_colour = input()
    if egg_colour == "red":
        red_eggs_counter += 1
    elif egg_colour == "orange":
        orange_eggs_counter += 1
    elif egg_colour == "blue":
        blue_eggs_counter += 1
    elif egg_colour == "green":
        green_eggs_counter += 1
max_eggs_counter = red_eggs_counter
color_winner = "red"
if orange_eggs_counter > red_eggs_counter:
    max_eggs_counter = orange_eggs_counter
    color_winner = "orange"
if blue_eggs_counter > red_eggs_counter:
    max_eggs_counter = blue_eggs_counter
    color_winner = "blue"
if green_eggs_counter > red_eggs_counter:
    max_eggs_counter = green_eggs_counter
    color_winner = "green"
print(f"Red eggs: {red_eggs_counter}")
print(f"Orange eggs: {orange_eggs_counter}")
print(f"Blue eggs: {blue_eggs_counter}")
print(f"Green eggs: {green_eggs_counter}")
print(f"Max eggs: {max_eggs_counter} -> {color_winner}")

