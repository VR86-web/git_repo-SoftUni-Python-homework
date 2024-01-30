from collections import deque

worms = deque([int(x) for x in input().split()])
holes = deque([int(x) for x in input().split()])

matches = 0

while True:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
        continue
    else:
        worm -= 3
        worms.append(worm)

print(worms)
print(holes)
