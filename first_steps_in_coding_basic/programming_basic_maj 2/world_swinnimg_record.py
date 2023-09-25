old_record = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())
delay = (distance_in_meters // 15) * 12.5
total_time = distance_in_meters * time_per_meter + delay
if total_time < old_record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds = total_time - old_record
    print(f"No, he failed! He was {seconds:.2f} seconds slower.")
