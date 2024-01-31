jobs_as_int = [int(x) for x in input().split(", ")]
jobs_idx = int(input())

max_num = float("inf")
clock_cycles = 0

while True:
    min_num = min(jobs_as_int)
    current_min_idx = jobs_as_int.index(min_num)
    clock_cycles += jobs_as_int[current_min_idx]
    if current_min_idx == jobs_idx:
        break
    else:
        jobs_as_int[current_min_idx] = max_num
print(clock_cycles)