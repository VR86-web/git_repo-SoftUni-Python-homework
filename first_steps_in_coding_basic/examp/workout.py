from math import ceil
number_of_days_training = int(input())
kilometers_running_first_day = float(input())
total_kilometers = kilometers_running_first_day
counter = 0
while counter < number_of_days_training:
    kilometers_running_next_day = int(input())
    kilometers_running_first_day = kilometers_running_first_day * (1 + kilometers_running_next_day / 100)
    total_kilometers += kilometers_running_first_day
    counter += 1
difference = abs(total_kilometers - 1000)
if total_kilometers >= 1000:
    print(f"You've done a great job running {ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(difference)} more kilometers")








