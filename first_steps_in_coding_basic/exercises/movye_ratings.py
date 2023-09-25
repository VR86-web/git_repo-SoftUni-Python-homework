
rating_counter = 0
number_of_movies = int(input())
best_movie = ""
maxrating = - 10

worst_movie = ""
minrating = 10
for movie in range(0, number_of_movies):
    current_movie = input()
    current_movie_rating = float(input())
    rating_counter += current_movie_rating
    if current_movie_rating > maxrating:
        best_movie = current_movie
        maxrating = current_movie_rating
    elif current_movie_rating < minrating:
        worst_movie = current_movie
        minrating = current_movie_rating
average_rating = rating_counter / number_of_movies
print(f"{best_movie} is with highest rating: {maxrating}")
print(f"{worst_movie} is with lowest rating: {minrating}")
print(f"Average rating: {average_rating:.1f}")

