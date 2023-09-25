number_of_group = int(input())
number_of_total_climbers = 0
people_climbing_musalla = 0
people_climbing_mont_blank = 0
people_climbing_kilimanjaro = 0
people_climbing_k_2 = 0
people_climbing_everest = 0

for group in range(number_of_group):
    climbers_in_group = int(input())

    if climbers_in_group <= 5:
        people_climbing_musalla += climbers_in_group
    elif climbers_in_group <= 12:
        people_climbing_mont_blank += climbers_in_group
    elif climbers_in_group <= 25:
        people_climbing_kilimanjaro += climbers_in_group
    elif climbers_in_group <= 40:
        people_climbing_k_2 += climbers_in_group
    elif climbers_in_group > 40:
        people_climbing_everest += climbers_in_group
    number_of_total_climbers += climbers_in_group

percent_of_people_climbing_musalla = people_climbing_musalla / number_of_total_climbers * 100
percent_of_people_climbing_mont_blank = people_climbing_mont_blank / number_of_total_climbers * 100
percent_of_people_climbing_kilimanjaro = people_climbing_kilimanjaro / number_of_total_climbers * 100
percent_of_people_climbing_k_2 = people_climbing_k_2 / number_of_total_climbers * 100
percent_of_people_climbing_everest = people_climbing_everest / number_of_total_climbers * 100

print(f"{percent_of_people_climbing_musalla:.2f}%")
print(f"{percent_of_people_climbing_mont_blank:.2f}%")
print(f"{percent_of_people_climbing_kilimanjaro:.2f}%")
print(f"{percent_of_people_climbing_k_2:.2f}%")
print(f"{percent_of_people_climbing_everest:.2f}%")

