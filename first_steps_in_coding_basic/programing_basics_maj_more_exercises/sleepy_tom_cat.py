number_of_day_offs_of_owner = int(input())

norm_minutes_game_with_cat_per_day = 30000 / 365
number_of_working_days = 365 - number_of_day_offs_of_owner
minutes_of_day_off = number_of_day_offs_of_owner * 24 * 60
minutes_game_with_cat_per_day_off = number_of_day_offs_of_owner * 127
minutes_game_with_cat_per_work_day = number_of_working_days * 63
total_time_game_with_cat = minutes_game_with_cat_per_day_off + minutes_game_with_cat_per_work_day
hours_of_time_game_with_cat = total_time_game_with_cat / 60
difference = abs(total_time_game_with_cat - 30000)
hours = difference / 60
minutes = difference % 60
if total_time_game_with_cat > 30000:

    print("Tom will run away")
    print(f"{int(hours)} hours and {minutes} minutes more for play")

else:

    print("Tom sleeps well")
    print(f"{int(hours)} hours and {minutes} minutes less for play")

