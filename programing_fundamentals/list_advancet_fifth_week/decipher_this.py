secret_message = input().split()
new_secret_message_list = []
for word in secret_message:
    letter_to_number = [letter for letter in word if letter.isdigit()]
    word_list = [current_word for current_word in word if current_word not in letter_to_number]
    first_letter = chr(int("".join(letter_to_number)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_word = first_letter + "".join(word_list)
    new_secret_message_list.append(new_word)
print(" ".join(new_secret_message_list))


