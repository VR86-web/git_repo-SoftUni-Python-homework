movie_name = input()
movie_packet = input()
num_of_tickets = int(input())
price = 0

if movie_name == "John Wick":
    if movie_packet == "Drink":
        price = 12
    elif movie_packet == "Popcorn":
        price = 15
    elif movie_packet == "Menu":
        price = 19
elif movie_name == "Star Wars":
    if movie_packet == "Drink":
        price = 18
    elif movie_packet == "Popcorn":
        price = 25
    elif movie_packet == "Menu":
        price = 30
elif movie_name == "Jumanji":
    if movie_packet == "Drink":
        price = 9
    elif movie_packet == "Popcorn":
        price = 11
    elif movie_packet == "Menu":
        price = 14
total_price = num_of_tickets * price

if movie_name == "Star Wars":
    if num_of_tickets >= 4:
        total_price = total_price * 0.7
if movie_name == "Jumanji":
    if num_of_tickets == 2:
        total_price = total_price * 0.85
print(f"Your bill is {total_price:.2f} leva.")