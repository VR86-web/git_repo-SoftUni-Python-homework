 #book = input()
 #number_of_books = -1
 #while True:
   # current_book = input()
    #number_of_books += 1
   #if current_book == book:

       # print(f"You checked {number_of_books} books and found it.")
       # break

   # elif current_book == "No More Books":

       # print("The book you search is not here!")
       # print(f"You checked {number_of_books} books.")
       # break

searched_book = input()
book_counter = 0
book_is_found = False
current_book = input()

while current_book != "No More Books":
    if current_book == searched_book:
        book_is_found = True
        break
    book_counter += 1
    current_book = input()
if book_is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")




