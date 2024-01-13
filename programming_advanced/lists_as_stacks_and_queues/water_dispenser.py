from collections import deque

quantity_of_water = int(input())
names_queue = deque()
name = input()
while name != "Start":
    names_queue.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        litters_requested = int(data[0])
        person = names_queue.popleft()
        if quantity_of_water >= litters_requested:
            print(f"{person} got water")
            quantity_of_water -= litters_requested
        else:
            print(f"{person} must wait")

    else:
        _, litters_to_add = data
        quantity_of_water += int(litters_to_add)

    command= input()

print(f"{quantity_of_water} liters left")
