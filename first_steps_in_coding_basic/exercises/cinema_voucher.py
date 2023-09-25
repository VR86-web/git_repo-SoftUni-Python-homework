voucher_price = int(input())
command = input()
price = 0
ticket_counter = 0
product_counter = 0
while command != "End":
    current_command = len(command)
    if current_command > 8:
        price = ord(command[0]) + ord(command[1])
    elif current_command <= 8:
        price = ord(command[0])
    voucher_price -= price
    if command == "End":
        break
    if voucher_price < 0:
        break
    if current_command > 8:
        ticket_counter += 1
    elif current_command <= 8:
        product_counter += 1
    command = input()
print(f"{ticket_counter}")
print(f"{product_counter}")








