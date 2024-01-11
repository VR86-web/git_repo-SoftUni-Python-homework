text = input()
encrypted_text = ""
for letter in text:
    current_letter_as_num = ord(letter) + 3
    encrypted_text += chr(current_letter_as_num)
print(encrypted_text)