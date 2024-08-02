import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, Avg, Max, F

from main_app.models import Director, Actor, Movie


# Create queries within functions


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(query_name & query_nationality)

    elif search_name is not None:
        query = query_name

    else:
        query = search_nationality

    directors = Director.objects.filter(query).order_by('full_name')
    if not directors:
        return ""

    result = []

    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()
    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    actor = Actor.objects.prefetch_related('starring_movies__actors').annotate(
        movies_count=Count('starring_movies'),
        movies_avg_rating=Avg('starring_movies__rating'),
    ).order_by('-movies_count', 'full_name').first()

    if not actor and not actor.movies_count:
        return ''

    movies = ", ".join(m.title for m in actor.starring_movies.all() if m)

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {movies}, movies average rating: {actor.movies_avg_rating:.1f}")


def get_actors_by_movies_count():
    actors = Actor.objects.prefetch_related('actor_movies__actors').annotate(
        num_movies=Count('actor_movies')
    ).order_by('-num_movies', 'full_name')[:3]

    if not actors and not actors[0].num_movies:
        return ""

    result = []
    for a in actors:
        result.append(f"{a.full_name1}, participated in {a.num_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects\
             .select_related('starring_actor')\
             .prefetch_related('actors')\
             .filter(is_awarded=True)\
             .order_by('-rating', 'title')\
             .first()

    if movie is None:
        return ''

    actors = movie.actors.order_by('full_name').values_list('full_name', flat=True)

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {', '.join(actors)}.")


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies_to_update:
        return "No ratings increased."

    updated_movies_count = movies_to_update.count()

    movies_to_update.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies_count} movies."
