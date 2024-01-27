from collections import deque


def fill_the_box(height, length, width, *cubes):
    space = height * length * width
    cubes = deque(cubes)

    while cubes[0] != "Finish":
        space -= cubes.popleft()

        if space < 0:
            cubes_left = sum(c for c in cubes if c != "finish")

            return f"No more free space! You have {cubes_left + abs(space)} more cubes."

    return f"There is free space in the box. You could put {space} more cubes."


print(fill_the_box(2, 8,2, 2, 1, 7, 3, 1, 5,"Finish"))