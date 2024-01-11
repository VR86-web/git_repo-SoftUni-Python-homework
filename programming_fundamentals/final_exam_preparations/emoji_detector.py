import re

text = input()
numbers_list = []
count_of_numbers = 1
pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})(\1)'
for letter in text:
    if letter.isdigit():
        numbers_list.append(int(letter))
for number in numbers_list:
    count_of_numbers *= number
matches = re.findall(pattern, text)
print(f"Cool threshold: {count_of_numbers}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for match in matches:
    count_of_matches = 0
    for letter in match[1]:
        count_of_matches += ord(letter)
    if count_of_matches > count_of_numbers:
        print("".join(match))


