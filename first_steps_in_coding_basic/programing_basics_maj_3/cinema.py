screening_type = input()
num_of_rows = int(input())
num_of_columns = int(input())

price = 0
if screening_type == "Premiere":
    price = 12.00
elif screening_type == "Normal":
    price = 7.50
elif screening_type == "Discount":
    price = 5.00
total_places = num_of_rows * num_of_columns
total_income = total_places * price
print(f"{total_income:.2f} leva")
