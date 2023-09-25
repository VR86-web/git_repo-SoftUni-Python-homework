player_name = input()
command = input()
points_counter = 301
successful_shoots_counter = 0
unsuccessful_shoots_counter = 0
while command != "Retire":
    points = int(input())
    if command == "Single":
        points_counter -= points
        successful_shoots_counter += 1
    elif command == "Double":
        points_counter -= points * 2
        successful_shoots_counter += 1
    elif command == "Triple":
        points_counter -= points * 3
        successful_shoots_counter += 1
    if points > points_counter:
        points = 0
        unsuccessful_shoots_counter += 1
    if points_counter == 0:
        print(f"{player_name} won the leg with {successful_shoots_counter} shots.")
        break
    command = input()
if command == "Retire":
    print(f"{player_name} retired after {unsuccessful_shoots_counter} unsuccessful shots.")



