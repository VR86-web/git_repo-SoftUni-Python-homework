from math import floor
number_of_tournaments = int(input())
starting_number_of_points = int(input())
average_points_counter = 0
wined_tournaments_counter = 0
for stage in range(number_of_tournaments):
    stage_reached = input()
    if stage_reached == "W":
        average_points_counter += 2000
        wined_tournaments_counter += 1
    elif stage_reached == "F":
        average_points_counter += 1200
    elif stage_reached == "SF":
        average_points_counter += 720
final_points = starting_number_of_points + average_points_counter
average_points = average_points_counter / number_of_tournaments
percentage_wined_tournaments = wined_tournaments_counter * 100 / number_of_tournaments
print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percentage_wined_tournaments:.2f}%")