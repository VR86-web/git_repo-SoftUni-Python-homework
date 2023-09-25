number_of_sold_games = int(input())
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
for current_game_name in range(number_of_sold_games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_counter += 1
    elif game_name == "Fornite":
        fornite_counter += 1
    elif game_name == "Overwatch":
        overwatch_counter +=1
    else:
        others_counter += 1
percent_sold_hearthstone = hearthstone_counter / number_of_sold_games * 100
percent_sold_fornite = fornite_counter / number_of_sold_games * 100
percent_sold_overwatch = overwatch_counter / number_of_sold_games * 100
percent_sold_others = others_counter / number_of_sold_games * 100
print(f"Hearthstone - {percent_sold_hearthstone:.2f}%")
print(f"Fornite - {percent_sold_fornite:.2f}%")
print(f"Overwatch - {percent_sold_overwatch:.2f}%")
print(f"Others - {percent_sold_others:.2f}%")


