
number_of_tournaments = int(input())
points_in_ranking_list = int(input())
total_points = 0
tournaments_won = 0
for tournament in range(number_of_tournaments):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        total_points += 2000
        tournaments_won += 1
    elif stage_of_tournament == "F":
        total_points += 1200
    elif stage_of_tournament == "SF":
        total_points += 720
average_points = total_points // number_of_tournaments
total_points += points_in_ranking_list
percent_of_won_tournaments = tournaments_won / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_of_won_tournaments:.2f}%")