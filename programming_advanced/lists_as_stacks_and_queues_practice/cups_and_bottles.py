from collections import deque

wasted_water = 0
cups_capacity = deque([int(x) for x in input().split()])
filled_bottles = deque([int(x) for x in input().split()])

while cups_capacity and filled_bottles:
    current_bottle_capacity = filled_bottles.pop()
    current_cup_capacity = cups_capacity.popleft()
    if current_cup_capacity <= current_bottle_capacity:
        wasted_water += current_bottle_capacity - current_cup_capacity
    else:
        cups_capacity.appendleft(current_cup_capacity - current_bottle_capacity)

if cups_capacity:
    print(f"Cups:", *cups_capacity)

else:
    print(f"Bottles:", *filled_bottles)

print(f"Wasted litters of water: {wasted_water}")
