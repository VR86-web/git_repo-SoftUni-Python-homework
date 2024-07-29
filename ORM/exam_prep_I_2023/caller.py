import os
import django
from django.db.models import Q

from main_app.models import Director

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions


def get_directors(search_name=None, search_nationality=None):

    if search_name is None and search_nationality is None:
        return ''

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name and search_nationality:
        query = Q(query_name) & Q(query_nationality)

    elif search_name:
        query = Q(query_name)

    else:
        query = Q(query_nationality)

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    result = []

    for director in directors:
        result.append(
            f"Director: {director.full_name}, "
            f"nationality: {director.nationality}, "
            f"experience: {director.years_of_experience}"
        )

    return '\n'.join(result)



