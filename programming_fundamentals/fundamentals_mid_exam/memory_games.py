sequence_of_elements = input().split()
command = input()
moves = 0
while command != "end":
    equal_elements = 0
    numbers = input(command).split()
    moves += 1
    for elements in sequence_of_elements:
        if command[0] == elements[1] and command[1] == elements[0]:
            equal_elements += 1
            sequence_of_elements.remove(elements[0])
            sequence_of_elements.remove(elements[1])
            print(f"Congrats! You have found matching elements - {equal_elements}!")
        if command[0] != elements[1] and command[1] != elements[0]:
            print("Try again!")
        if len(sequence_of_elements) == 0:
            print(f"You have won in {moves} turns!")
            break
        if command[0] == "end":
            print("Sorry you lose :(")
            print(f"{sequence_of_elements}")
            break
    command = input()