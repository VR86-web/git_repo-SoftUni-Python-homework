pool_volume = int(input())
debit_of_first_pipe = int(input())
debit_of_second_pipe = int(input())
hours_missing_worker = float(input())

liters_per_hour_firs_pipe = hours_missing_worker * debit_of_first_pipe
liters_per_hour_second_pipe = hours_missing_worker * debit_of_second_pipe
total_liters_per_hour = liters_per_hour_firs_pipe + liters_per_hour_second_pipe
percentage_of_first_pipe = liters_per_hour_firs_pipe / total_liters_per_hour * 100
percentage_of_second_pipe = liters_per_hour_second_pipe / total_liters_per_hour * 100
total_percentage_of_pool = total_liters_per_hour / pool_volume * 100
difference = total_liters_per_hour - pool_volume
if total_liters_per_hour <= pool_volume:
    print(f"The pool is {total_percentage_of_pool:.2f}% full. "
          f"Pipe 1: {percentage_of_first_pipe:.2f}%. Pipe 2: {percentage_of_second_pipe:.2f}%.")
else:
    print(f"For {hours_missing_worker:.2f} hours the pool overflow {difference:.2f} liters.")


