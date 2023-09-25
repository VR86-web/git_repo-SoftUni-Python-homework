number_of_sold_games = int(input())
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
game_name = input()
while game_name != "Hearthstone" or game_name != "Fornite" or game_name != "Overwatch":
    others_counter += 1
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_counter += 1
    elif game_name == "Fornite":
        fornite_counter += 1
    elif game_name == "Overwatch":
        overwatch_counter += 1
    hearthstone_percentage = hearthstone_counter / 100
    fornite_percentage = fornite_counter / 100
    overwatch_percentage = overwatch_counter / 100
    others_percentage = others_counter / 100
    print(f"Hearthstone - {hearthstone_percentage:.2f}%")
    print(f"Fornite - {fornite_percentage:.2f}%")
    print(f"Overwatch - {overwatch_percentage:.2f}%")
    print(f"Others - {others_percentage:.2f}%")



