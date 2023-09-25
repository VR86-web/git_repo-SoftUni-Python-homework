floors = int(input())
rooms_per_floor = int(input())

for floor in reversed(range(1, floors + 1)):
    rooms_type = "A" if floor % 2 else "O"
    if floor == floors:
        rooms_type = "L"
    for room in range(rooms_per_floor):
        room_name = f"{rooms_type}{floor}{room}"
        print(room_name, end=" ")

    print()

