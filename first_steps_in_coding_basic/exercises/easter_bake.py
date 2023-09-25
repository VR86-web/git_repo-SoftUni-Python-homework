from math import ceil

number_of_easter_breads = int(input())
quantity_sugar_counter = 0
quantity_flour_counter = 0
max_flour = 0
max_sugar = 0
for bread in range(number_of_easter_breads):
    quantity_sugar = int(input())
    quantity_flour = int(input())
    quantity_sugar_counter += quantity_sugar
    quantity_flour_counter += quantity_flour
    if quantity_sugar > max_sugar:
        max_sugar = quantity_sugar
    if quantity_flour > max_flour:
        max_flour = quantity_flour
packet_sugar = quantity_sugar_counter / 950
packet_flour = quantity_flour_counter / 750
print(f"Sugar: {ceil(packet_sugar)}")
print(f"Flour: {ceil(packet_flour)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")