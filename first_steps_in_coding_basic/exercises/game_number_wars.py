first_player_name = input()
second_player_name = input()
command = input()
first_player_points_counter = 0
second_player_points_counter = 0

while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        first_player_points_counter += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        second_player_points_counter += second_player_card - first_player_card
    elif first_player_card == second_player_card:
        print("Number wars!")
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print(f"{first_player_name} is winner with {first_player_points_counter} points")
            break
        elif second_player_card > first_player_card:
            print(f"{second_player_name} is winner with {second_player_points_counter} points")
            break
    command = input()
if command == "End of game":
    print(f"{first_player_name} has {first_player_points_counter} points")
    print(f"{second_player_name} has {second_player_points_counter} points")



