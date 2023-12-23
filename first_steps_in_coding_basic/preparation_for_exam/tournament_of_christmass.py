number_days_of_tournament = int(input())
total_money = 0
win_counter = 0
lose_counter = 0

for current_day in range(number_days_of_tournament):
    current_number_of_wins = 0
    current_number_of_lost = 0
    current_money = 0
    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            win_counter += 1
            current_money += 20
            current_number_of_wins += 1
        elif result == "lose":
            current_number_of_lost += 1
    if current_number_of_wins > current_number_of_lost:
        total_money += current_money + (current_money * 0.10)
    else:
        total_money += current_money
    lose_counter += current_number_of_lost

if win_counter > lose_counter:
    total_money += total_money * 0.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
