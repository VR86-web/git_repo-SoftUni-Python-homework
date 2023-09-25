last_sector = input()
num_of_rows_in_first_sector = int(input())
num_of_seats_of_odd_row = int(input())
start_sector = 65
start_seats = 97
counter = 0
for sectors in range(start_sector, ord(last_sector) + 1):
    