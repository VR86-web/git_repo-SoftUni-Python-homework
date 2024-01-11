text = input()
digits = ""
strings = ""
rest = ""
for letter in text:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        strings += letter
    else:
        rest += letter
print(digits)
print(strings)
print(rest)