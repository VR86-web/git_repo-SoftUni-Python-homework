from collections import deque


initial_fuel = [int(x)for x in input().split()]
additional_consumption_index = deque([int(x)for x in input().split()])
amount_of_fuel_needed = deque([int(x)for x in input().split()])

reached_altitudes = 0

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:

    current_fuel = initial_fuel[-1]
    current_consumption_index = additional_consumption_index[0]
    current_needed_fuel = amount_of_fuel_needed[0]

    if (current_fuel - current_consumption_index) >= current_needed_fuel:
        initial_fuel.pop()
        additional_consumption_index.popleft()
        amount_of_fuel_needed.popleft()
        reached_altitudes += 1
        print(f"John has reached: Altitude {reached_altitudes}")

    else:
        print(f"John did not reach: Altitude {reached_altitudes + 1}")
        break

if initial_fuel and reached_altitudes:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, reached_altitudes + 1)])}")

elif initial_fuel and not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

if not initial_fuel:
    print("John has reached all the altitudes and managed to reach the top!")


