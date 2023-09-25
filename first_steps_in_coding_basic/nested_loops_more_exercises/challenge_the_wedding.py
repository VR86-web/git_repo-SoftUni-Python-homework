number_of_male_clients = int(input())
number_of_female_clients = int(input())
max_number_of_tables = int(input())
combinations_counter = 0
for male in range(1, number_of_male_clients + 1):
    for female in range(1, number_of_female_clients + 1):
        combinations_counter += 1
        if combinations_counter >= max_number_of_tables:
            print(f"({male} <-> {female})", end=" ")
            break
        print(f"({male} <-> {female})", end=" ")




