number_of_snowballs = int(input())
snowball_weight_max_counter = 0
snowball_speed_max_counter = 0
snowball_quality_max_counter = 0
snowball_max_value = 0
for snowballs in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_speed = int(input())
    snowball_quality = int(input())
    current_snowball = (snowball_weight / snowball_speed) ** snowball_quality
    if current_snowball > snowball_max_value:
        snowball_max_value = current_snowball
        snowball_weight_max_counter = snowball_weight
        snowball_speed_max_counter = snowball_speed
        snowball_quality_max_counter = snowball_quality
print(f"{snowball_weight_max_counter} : {snowball_speed_max_counter} = "
      f"{int(snowball_max_value)} ({snowball_quality_max_counter})")
