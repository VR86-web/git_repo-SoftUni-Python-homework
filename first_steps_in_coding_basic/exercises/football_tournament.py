football_team_name = input()
number_of_played_games = int(input())
win_games_counter = 0
draw_result_counter = 0
loose_result_counter = 0

if number_of_played_games == 0:
    print(f"{football_team_name} hasn't played any games during this season.")
elif number_of_played_games > 0:
    for result in range(number_of_played_games):
        current_result = input()
        if current_result == "W":
            win_games_counter += 1
        elif current_result == "D":
            draw_result_counter += 1
        elif current_result == "L":
            loose_result_counter += 1
    points_earned = win_games_counter * 3 + draw_result_counter
    win_rate = win_games_counter / number_of_played_games * 100
    print(f"{football_team_name} has won {points_earned} points during this season.")
    print("Total stats:")
    print(f"## W: {win_games_counter}")
    print(f"## D: {draw_result_counter}")
    print(f"## L: {loose_result_counter}")
    print(f"Win rate: {win_rate:.2f}%")


