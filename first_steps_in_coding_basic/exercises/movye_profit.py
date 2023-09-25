movie_name = input()
num_of_days = int(input())
num_of_tickets = int(input())
price_per_ticket = float(input())
cinema_percentage = int(input())
income = price_per_ticket * num_of_tickets * num_of_days
income_for_cinema = income * cinema_percentage / 100
total_income = income - income_for_cinema
print(f"The profit from the movie {movie_name} is {total_income:.2f} lv.")