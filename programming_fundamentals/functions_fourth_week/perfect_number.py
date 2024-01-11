def perfect_number(some_number: int) -> str:
    numbers_counter = 0
    for current_number in range(1, some_number):
        if some_number % current_number == 0:
            numbers_counter += current_number
    if some_number == numbers_counter:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
result = perfect_number(number)
print(result)