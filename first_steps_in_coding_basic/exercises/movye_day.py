time_for_shooting = int(input())
num_of_scenes = int(input())
scene_duration = int(input())
terrain_preparation = time_for_shooting * 0.15
shooting_day_duration = (num_of_scenes * scene_duration) + terrain_preparation
left_or_needed_time = abs(time_for_shooting - shooting_day_duration)
if shooting_day_duration <= time_for_shooting:
    print(f"You managed to finish the movie on time! You have {round(left_or_needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(left_or_needed_time)} minutes.")