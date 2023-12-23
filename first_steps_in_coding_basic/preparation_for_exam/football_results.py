first_game_result = input()
second_game_result = input()
third_game_result = input()
home_goals1, away_goals1 = first_game_result[0], first_game_result[2]
home_goals2, away_goals2 = second_game_result[0], second_game_result[2]
home_goals3, away_goals3 = third_game_result[0], third_game_result[2]
wins = int(home_goals1 > away_goals1) + int(home_goals2 > away_goals2) + int(home_goals3 > away_goals3)
losses = int(home_goals1 < away_goals1) + int(home_goals2 < away_goals2) + int(home_goals3 < away_goals3)
draws = int(home_goals1 == away_goals1) + int(home_goals2 == away_goals2) + int(home_goals3 == away_goals3)
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f" Drawn games: {draws}")

