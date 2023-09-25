number_of_easter_breads = int(input())
max_points = 0
best_baker = ""
for name in range(number_of_easter_breads):
    new_best_baker = False
    name_of_baker = input()
    points_counter = 0
    while True:
        command = input()
        if command == "Stop":
            print(f"{name_of_baker} has {points_counter} points.")
            break
        points_for_bread = int(command)
        points_counter += points_for_bread
        if points_counter > max_points:
            max_points = points_counter
            best_baker = name_of_baker
            new_best_baker = True
    if new_best_baker:
        print(f"{best_baker} is the new number 1!")
print(f"{best_baker} won competition with {max_points} points!")




