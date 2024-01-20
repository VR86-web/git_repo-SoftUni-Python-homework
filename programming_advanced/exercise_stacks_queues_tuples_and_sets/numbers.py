first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

command_function = {
    "Add First": lambda x: [first_sequence.add(int(el)) for el in x],
    "Add Second": lambda x: [second_sequence.add(int(el)) for el in data],
    "Remove First": lambda x: [first_sequence.discard(int(el)) for el in data],
    "Remove Second": lambda x: [second_sequence.discard(int(el)) for el in data],
    "Check Subset": lambda x: print(first_sequence.issubset(second_sequence) or
                                    second_sequence.issubset(first_sequence))
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command
    command_function[command](data)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

