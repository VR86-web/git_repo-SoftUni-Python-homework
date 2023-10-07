last_sector = input()
num_of_rows_in_first_sector = int(input())
num_of_seats_of_odd_row = int(input())
start_sector = 65
start_seats = 97
counter = 0
for sectors in range(start_sector, ord(last_sector) + 1):
    for rows in range(1, num_of_rows_in_first_sector + 1):
        if rows % 2 != 0:
            for seats in range(start_seats, (start_seats + num_of_seats_of_odd_row)):
                print(f"{chr(sectors)}{rows}{chr(seats)}")
                counter += 1
        elif rows % 2 == 0:
            for seats in range(start_seats, (start_seats + num_of_seats_of_odd_row + 2)):
                print(f"{chr(sectors)}{rows}{chr(seats)}")
                counter += 1
    num_of_rows_in_first_sector += 1
print(counter)


