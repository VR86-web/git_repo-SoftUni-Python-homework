from math import ceil

height_of_wall = int(input())
width_of_wall = int(input())
percent_not_painted_area = int(input())
painted_square_meters = height_of_wall * width_of_wall * 4
total_painted_square_meters = ceil(painted_square_meters - (painted_square_meters * percent_not_painted_area / 100))
stop_painting = False
command = input()
while command != "Tired!":
    liters_of_paint = int(command)
    total_painted_square_meters -= liters_of_paint
    if total_painted_square_meters <= 0:
        break
    command = input()
    if command == "Tired!":
        stop_painting = True

if stop_painting:
    print(f"{total_painted_square_meters} quadratic m left.")
elif total_painted_square_meters == 0:
    print("All walls are painted! Great job, Pesho!")
elif total_painted_square_meters < 0:
    print(f"All walls are painted and you have {abs(total_painted_square_meters)} l paint left!")




