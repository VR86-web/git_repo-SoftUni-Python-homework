def best_list_pureness(*args):
    numbers = args[0]
    rotations = args[1]
    best_pureness = 0
    best_rotation = 0

    for rotation in range(rotations + 1):
        pureness = 0
        for idx, num in enumerate(numbers):
            pureness += idx * num
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation

        numbers.insert(0, numbers.pop())
    return f'Best pureness {best_pureness} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


