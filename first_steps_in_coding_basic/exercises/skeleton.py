control_minutes = int(input())
control_seconds = int(input())
chute_length_in_meters = float(input())
seconds_per_hundred_meters = float(input())
total_control_time = control_minutes * 60 + control_seconds
time_reduction = (chute_length_in_meters / 120) * 2.5
competitors_time = (chute_length_in_meters / 100) * seconds_per_hundred_meters - time_reduction
if competitors_time <= total_control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitors_time:.3f}.")
else:
    needed_time = competitors_time - total_control_time
    print(f"No, Marin failed! He was {needed_time:.3f} second slower.")
