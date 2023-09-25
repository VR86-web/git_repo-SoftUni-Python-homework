anual_tax = int(input())
sneakers_price = anual_tax - anual_tax * 40 / 100
dress_price = sneakers_price * 0.8
ball_price = dress_price / 4
accessories_price = ball_price / 5
total_sum = anual_tax + sneakers_price \
            + dress_price + ball_price + accessories_price
print(total_sum)