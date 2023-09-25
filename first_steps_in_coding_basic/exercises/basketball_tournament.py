tournament_name = input()
game_counter = 0
game_lost_counter = 0
game_win_counter = 0
total_game_counter = 0
while tournament_name != "End of tournaments":
    number_of_games = int(input())
    for game in range(number_of_games):
        desi_team_points = int(input())
        second_team_points = int(input())
        game_counter += 1
        total_game_counter += 1
        points_difference = abs(desi_team_points - second_team_points)
        if desi_team_points > second_team_points:
            points_difference = desi_team_points - second_team_points
            game_win_counter += 1
            print(f"Game {game_counter} of tournament {tournament_name}: win with {points_difference} points.")
        if desi_team_points < second_team_points:
            game_lost_counter += 1
            print(f"Game {game_counter} of tournament {tournament_name}: lost with {points_difference} points.")
    tournament_name = input()
    game_counter = 0
game_win_percentage = (game_win_counter / total_game_counter) * 100
game_lost_percentage = (game_lost_counter / total_game_counter) * 100
if tournament_name == "End of tournaments":
    print(f"{game_win_percentage:.2f}% matches win")
    print(f"{game_lost_percentage:.2f}% matches lost")



