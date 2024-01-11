word = input()
while word != "End":
    if word != "SoftUni":
        new_string = ""
        for character in word:
            new_string += character * 2
        print(new_string)
    word = input()