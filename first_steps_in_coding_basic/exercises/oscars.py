actor_name = input()
academy_points = float(input())
jury_number = int(input())
points_counter = 0
oscar_nomination = False
current_points_counter = 0
total_points_counter = 0
for jury in range(jury_number):
    name_of_jury = input()
    points_from_jury = float(input())
    points_counter = (len(name_of_jury) * points_from_jury) / 2
    current_points_counter += points_counter
    total_points_counter = current_points_counter + academy_points
    if total_points_counter > 1250.5:
        oscar_nomination = True
        break

if oscar_nomination:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points_counter:.1f}!")
else:
    needed_points = 1250.5 - total_points_counter
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
