names_of_the_gifts = input().split()
command = input()
while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for words in range(len(names_of_the_gifts)):
            if command[1] in names_of_the_gifts[words]:
                names_of_the_gifts[words] = "None"
    elif "Required" in command:
        for words in range(len(names_of_the_gifts)):
            if words == int(command[2]):
                names_of_the_gifts[words] = command[1]
    elif "JustInCase" in command:
        names_of_the_gifts[-1] = command[1]
    command = input()
while "None" in names_of_the_gifts:
    names_of_the_gifts.remove("None")
for words in names_of_the_gifts:
    print(words, end=" ")


