from math import ceil

name_of_serial = input()
episode_time = int(input())
break_time = int(input())
lunch_time = break_time / 8
rest_time = break_time / 4
free_time = break_time - lunch_time - rest_time
needed_time = ceil (abs(free_time - episode_time))
if free_time >= episode_time:
    print(f"You have enough time to watch {name_of_serial} and left with {needed_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {needed_time} more minutes.")