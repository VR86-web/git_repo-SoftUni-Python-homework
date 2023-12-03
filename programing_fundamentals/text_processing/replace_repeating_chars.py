sequence_of_letters = input()
final_message = ""
last_added_character = ""
for letter in sequence_of_letters:
    if letter != last_added_character:
        final_message += letter
        last_added_character = letter
print(final_message)