import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review

# Create and check models


def find_books_by_genre_and_language(book_genre, book_language):
    books = Book.objects.filter(genre=book_genre, language=book_language)
    return books


def find_authors_nationalities():
    authors = Author.objects.exclude(nationality=None)
    return '\n'.join(f"{author.first_name} {author.last_name} is {author.nationality}" for author in authors)


def order_books_by_year():
    books = Book.objects.all().order_by('publication_year', 'title')
    return '\n'.join(f"{book.publication_year} year: {book.title} by {book.author}" for book in books)


def delete_review_by_id(review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return f"Review by {review.reviewer_name} was deleted"


def filter_authors_by_nationalities(nationality):
    result = []
    authors = Author.objects.filter(nationality=nationality).order_by('first_name', 'last_name')

    for author in authors:
        result.append(author.biography) \
            if author.biography is not None else result.append(f"{author.first_name} {author.last_name}")

    return '\n'.join(result)


def filter_authors_by_birth_year(first_year, second_year):
    authors = Author.objects.filter(birth_date__year__range=(first_year, second_year)).order_by('-birth_date')
    return '\n'.join(f"{author.birth_date}: {author.first_name} {author.last_name}" for author in authors)


def change_reviewer_name(reviewer_name, new_name):
    Review.objects.filter(reviewer_name=reviewer_name).update(reviewer_name=new_name)
    return Review.objects.all()



