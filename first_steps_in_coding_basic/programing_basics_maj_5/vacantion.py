money_needed_for_traveling = float(input())
available_money = float(input())
total_days_counter = 0
spend_money_counter = 0
spending_too_many_days_in_a_row = False

while available_money < money_needed_for_traveling:
    action = input()
    current_money = float(input())
    total_days_counter += 1
    if action == "spend":
        spend_money_counter += 1
        if spend_money_counter == 5:
            spending_too_many_days_in_a_row = True
            break
        available_money -= current_money
        if available_money < 0:
            available_money = 0
    elif action == "save":
        available_money += current_money
        spend_money_counter = 0
if spending_too_many_days_in_a_row:
    print("You can't save the money.")
    print(total_days_counter)
else:
    print(f"You saved the money for {total_days_counter} days.")
