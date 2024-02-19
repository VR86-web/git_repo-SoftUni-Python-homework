from collections import deque

amount_of_money = [int(x) for x in input().split()]
pieces_of_foods = deque(int(x) for x in input(). split())

eaten_food_counter = 0

while amount_of_money and pieces_of_foods:
    money = amount_of_money.pop()
    piece_of_food = pieces_of_foods.popleft()

    if money == piece_of_food:
        eaten_food_counter += 1
    elif money > piece_of_food:
        eaten_food_counter += 1
        difference = money - piece_of_food
        if len(amount_of_money) >= 1:
            amount_of_money[-1] += difference
    else:
        continue

if eaten_food_counter >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food_counter} foods.")

elif eaten_food_counter < 1:
    print("Henry remained hungry. He will try next weekend again.")

elif eaten_food_counter == 1:
    print("Henry ate: 1 food.")

else:
    print(f"Henry ate: {eaten_food_counter} foods.")
