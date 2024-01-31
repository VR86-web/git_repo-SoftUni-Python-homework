def list_manipulator(numbers, *args):
    first_command = args[0]
    second_command = args[1]
    given_numbers = [int(x) for x in args[2:]]

    if first_command == "remove":
        nums_to_remove = 1
        if second_command == "beginning":
            if given_numbers:
                nums_to_remove = given_numbers.pop()
            numbers = numbers[nums_to_remove:]

        else:
            if given_numbers:
                nums_to_remove = given_numbers.pop()
            for _ in range(nums_to_remove):
                numbers.pop()

    elif first_command == "add":
        if second_command == "beginning":
            given_numbers.extend(numbers)
            numbers = given_numbers
        else:
            numbers.extend(given_numbers)

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))