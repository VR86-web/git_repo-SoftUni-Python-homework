numbers = tuple([float(x)for x in input().split()])
same_values = {}

for num in numbers:
    if num not in same_values:
        same_values[num] = numbers.count(num)

for key, value in same_values.items():
    print(f"{key} - {value} times")