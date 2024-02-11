from collections import deque

worms = [int(el) for el in input().split()]
holes = deque(int(el) for el in input().split())

all_worms_count = len(worms)
matches = 0

while worms and holes:
    worm = worms[-1]
    hole = holes[0]

    if worm == hole:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and matches == all_worms_count:
    print("Every worm found a suitable hole!")
elif not worms and matches != all_worms_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
