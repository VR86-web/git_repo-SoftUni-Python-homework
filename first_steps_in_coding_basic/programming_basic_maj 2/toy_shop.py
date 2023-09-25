needed_money = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
total_sum = puzzles * 2.60 \
            + dolls * 3 \
            + bears * 4.10 \
            + minions * 8.20 \
            + trucks * 2
total_toys = puzzles + dolls + bears + minions + trucks
if total_toys >= 50:
    total_sum = total_sum * 0.75
total_sum= total_sum * 0.90
difference = abs(total_sum - needed_money)
if total_sum >= needed_money:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
