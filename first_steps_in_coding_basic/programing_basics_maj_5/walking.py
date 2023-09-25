taken_steps = 0

while taken_steps < 10000:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        taken_steps += steps_to_home
        break
    current_steps = int(command)
    taken_steps += current_steps
difference = abs(taken_steps - 10000)
if taken_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")




