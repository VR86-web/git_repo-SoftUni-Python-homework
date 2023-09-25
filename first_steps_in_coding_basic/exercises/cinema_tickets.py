student_ticket_counter = 0
standard_ticket_counter = 0
kid_ticket_counter = 0
total_sold_ticket_counter = 0
movie_name = input()

while movie_name != "Finish":
    free_seats = int(input())
    busy_seats = 0
    for i in range(free_seats):
        type_of_ticket = input()
        if type_of_ticket == "student":
            student_ticket_counter += 1
        elif type_of_ticket == "standard":
            standard_ticket_counter += 1
        elif type_of_ticket == "kid":
            kid_ticket_counter += 1
        elif type_of_ticket == "End":
            break
        total_sold_ticket_counter += 1
        busy_seats += 1
    percentage_full_hall = busy_seats / free_seats * 100
    print(f"{movie_name} - {percentage_full_hall:.2f}% full.")
    movie_name = input()
percentage_student_tickets = student_ticket_counter / total_sold_ticket_counter * 100
percentage_standard_tickets = standard_ticket_counter / total_sold_ticket_counter * 100
percentage_kid_tickets = kid_ticket_counter / total_sold_ticket_counter * 100
print(f"Total tickets: {total_sold_ticket_counter}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")




