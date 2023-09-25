from math import floor

minutes_of_control = int(input())
seconds_of_control = int(input())
length_in_meters = float(input())
seconds_per_100_meters = int(input())

total_time_of_control = minutes_of_control * 60 + seconds_of_control
delay_time = length_in_meters / 120
total_delay_time = delay_time * 2.5
competitor_time = (length_in_meters / 100) * floor(delay_time) - total_delay_time
missing_time = abs(total_time_of_control - competitor_time)
if competitor_time <= total_time_of_control:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitor_time:.3f}.")
elif competitor_time > total_time_of_control:
    print(f"No, Marin failed! He was {missing_time:.3f} second slower.")
