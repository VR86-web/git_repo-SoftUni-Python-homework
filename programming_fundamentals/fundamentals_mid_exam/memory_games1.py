def main():
    sequence_of_elements = input().split()
    moves = 0

    while True:
        moves += 1
        command = input()
        if command == "end":
            print("Sorry you lose :(")
            print(f"{' '.join(sequence_of_elements)}")
            break

        index1, index2 = map(int, command.split())

        if is_invalid_input(index1, index2, sequence_of_elements):
            handle_invalid_input(sequence_of_elements, moves)
        else:
            handle_valid_input(index1, index2, sequence_of_elements, moves)


def is_invalid_input(index1, index2, sequence):
    return (
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(sequence)
        or index2 >= len(sequence)
    )


def handle_invalid_input(sequence_of_elements, moves):
    mid_index = len(sequence_of_elements) // 2
    sequence_of_elements.insert(mid_index, f"-{moves}a" )
    sequence_of_elements.insert(mid_index, f"-{moves}a")
    print("Invalid input! Adding additional elements to the board")


def handle_valid_input(index1, index2, sequence_of_elements, moves):
    if sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index1]}!")
        second_el = sequence_of_elements[index2]
        sequence_of_elements.pop(index1)
        sequence_of_elements.remove(second_el)
    else:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {moves} turns!")
        exit()


main()