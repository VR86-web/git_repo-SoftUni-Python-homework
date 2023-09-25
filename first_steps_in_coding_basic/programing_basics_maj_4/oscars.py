name_of_actor = input()
points_from_academy = float(input())
number_of_jury = int(input())
total_points = points_from_academy

for current_grade in range(number_of_jury):
    name_of_jury = input()
    points_from_jury = float(input())
    current_points = len(name_of_jury) * points_from_jury / 2
    total_points += current_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")
