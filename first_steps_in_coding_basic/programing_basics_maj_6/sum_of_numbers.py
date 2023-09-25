start_of_interval = int(input())
finish_of_interval = int(input())
magik_number = int(input())
combination_counter = 0
break_condition = False

for x in range(start_of_interval, finish_of_interval + 1):
    for y in range(start_of_interval, finish_of_interval + 1):
        combination_counter += 1
        if x + y == magik_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {magik_number})")
            break_condition = True
            break
    if break_condition:
        break
if not break_condition:
    print(f"{combination_counter} combinations - neither equals {magik_number}")
