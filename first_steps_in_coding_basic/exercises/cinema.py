hall_capacity = int(input())
command = input()
people_counter = 0
ticket_price_counter = 0
the_hall_is_full = False
while command != "Movie time!":
    number_of_people = int(command)
    people_counter += number_of_people
    ticket_price_counter = people_counter * 5
    if number_of_people % 3 == 0:
        ticket_price_counter -= 5
    if people_counter > hall_capacity:
        the_hall_is_full = True
        break
    command = input()
if the_hall_is_full:
    print(f"The cinema is full.")
    print(f"Cinema income - {ticket_price_counter} lv.")
if command == "Movie time!":
    seats_left = hall_capacity - people_counter
    print(f"There are {seats_left} seats left in the cinema.")
    print(f"Cinema income - {ticket_price_counter} lv.")