def characters(first_character: str, second_character: str) -> list:
    character_list = []
    for numbers in range(ord(first_character) + 1, ord(second_character)):
        character_list.append(chr(numbers))
    return character_list


first_char = input()
second_char = input()
final_result = characters(first_char, second_char)
print(" ".join(final_result))