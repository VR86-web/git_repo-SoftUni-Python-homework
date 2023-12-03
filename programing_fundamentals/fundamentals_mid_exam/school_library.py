book_names_list = input().split("&")
instructions = input().split(" | ")
while instructions[0] != "Done":
    command = instructions[0]
    if command == "Add Book":
        book_name = instructions[1]
        if book_name not in book_names_list:
            book_names_list.insert(0, book_name)
    elif command == "Take Book":
        book_name = instructions[1]
        if book_name in book_names_list:
            book_names_list.remove(book_name)
    elif command == "Swap Book":
        book_1 = instructions[1]
        book_2 = instructions[2]
        if book_1 in book_names_list and book_2 in book_names_list:
            i = book_names_list.index(book_1)
            x = book_names_list.index(book_2)
            book_names_list[i], book_names_list[x] = book_names_list[x], book_names_list[i]
    elif command == "Insert Book":
        book_name = instructions[1]
        book_names_list.append(book_name)
    elif command == "Check Book":
        index = int(instructions[1])
        if index in range(len(book_names_list)):
            print(book_names_list[index])

    instructions = input().split("|")

print(", ".join(book_names_list))
