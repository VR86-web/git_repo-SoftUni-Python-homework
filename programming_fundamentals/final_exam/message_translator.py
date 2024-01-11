import re

number_of_messages = int(input())
for message in range(number_of_messages):
    current_message = input()
    pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
    matches = re.match(pattern, current_message)

    if matches is None:
        print("The message is invalid")
        continue

    second_part_of_message = []

    for match in matches[2]:
        second_part_of_message.append(str(ord(match)))
    print(f"{matches[1]}: {' '.join(second_part_of_message)}")



