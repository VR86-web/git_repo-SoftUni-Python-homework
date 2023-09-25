change_money = float(input())

change_money = int(change_money * 100)
coins_counter = 0
coins_counter += change_money // 200
change_money = change_money % 200
coins_counter += change_money // 100
change_money = change_money % 100
coins_counter += change_money // 50
change_money = change_money % 50
coins_counter += change_money // 20
change_money = change_money % 20
coins_counter += change_money // 10
change_money = change_money % 10
coins_counter += change_money // 5
change_money = change_money % 5
coins_counter += change_money // 2
change_money = change_money % 2
coins_counter += change_money // 1
change_money = change_money % 1
print(coins_counter)