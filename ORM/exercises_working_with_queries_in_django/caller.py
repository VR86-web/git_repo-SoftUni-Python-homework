import os
from typing import List

import django
from django.db.models import Case, When, Value

from main_app.choices import MealTypeChoices, DungeonChoices, WorkoutChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models


from main_app.models import ArtworkGallery, Laptop, OperationSystemChoices, ChessPlayer, Meal, Dungeon, Workout


# Create and check models


def show_highest_rated_art():
    highest_rated_art = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return str(highest_rated_art)


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art
    ])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=('Asus', 'Lenovo')).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)


def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value(OperationSystemChoices.WINDOWS)),
            When(brand='Apple', then=Value(OperationSystemChoices.MACOS)),
            When(brand='Dell', then=Value(OperationSystemChoices.LINUX)),
            When(brand='Lenovo', then=Value(OperationSystemChoices.CHROME_OS))
        )
    )


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__ld=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title='regular player')


def set_new_chefs():
    Meal.objects.filter(meal_type=MealTypeChoices.BREAKFAST).update(chef='Gordon Ramsay')
    Meal.objects.filter(meal_type=MealTypeChoices.LUNCH).update(chef='Julia Child')
    Meal.objects.filter(meal_type=MealTypeChoices.DINNER).update(chef='Jamie Oliver')
    Meal.objects.filter(meal_type=MealTypeChoices.SNACK).update(chef='Thomas Keller')


def set_new_preparation_times():
    Meal.objects.filter(meal_type=MealTypeChoices.BREAKFAST).update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type=MealTypeChoices.LUNCH).update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type=MealTypeChoices.DINNER).update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type=MealTypeChoices.SNACK).update(preparation_time='5 minutes')


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=("Breakfast", "Dinner")).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).delete()


def show_hard_dungeons():
    hard_dungeons = Dungeon.objects.filter(difficulty=DungeonChoices.EASY).order_by('-location')

    return '\n'.join(str(x) for x in hard_dungeons)


def bulk_create_dungeons(args: List[Dungeon]):
    Dungeon.objects.bulk_create(args)


def update_dungeon_names():
    Dungeon.objects.filter(difficulty=DungeonChoices.EASY).update(name='The Erased Thombs')
    Dungeon.objects.filter(difficulty=DungeonChoices.MEDIUM).update(name='The Coral Labyrinth')
    Dungeon.objects.filter(difficulty=DungeonChoices.HARD).update(name='The Lost Haunt')


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty=DungeonChoices.EASY).update(boss_health=500)


def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty=DungeonChoices.EASY).update(recommended_level=25)
    Dungeon.objects.filter(difficulty=DungeonChoices.MEDIUM).update(recommended_level=50)
    Dungeon.objects.filter(difficulty=DungeonChoices.HARD).update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location='Enchanted Maze')
    Dungeon.objects.filter(recommended_level=50).update(location='Grimstone Mines')
    Dungeon.objects.filter(recommended_level=75).update(location='Shadowed Abyss')


def show_workouts():
    workouts = (Workout.objects.filter(workout_type__in=(WorkoutChoices.CALISTHENICS, WorkoutChoices.CROSSFIT)).order_by('id'))

    return '\n'.join(str(x) for x in workouts)


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type=WorkoutChoices.CARDIO, difficulty='High').order_by('instructor')


def set_new_instructors():
    Workout.objects.filter(workout_type=WorkoutChoices.CARDIO).update(instructor='John Smith')
    Workout.objects.filter(workout_type=WorkoutChoices.STRENGTH).update(instructor='Michael Williams')
    Workout.objects.filter(workout_type=WorkoutChoices.YOGA).update(instructor='Emily Johnson')
    Workout.objects.filter(workout_type=WorkoutChoices.CROSSFIT).update(instructor='Sarah Davis')
    Workout.objects.filter(workout_type=WorkoutChoices.CALISTHENICS).update(instructor='Chris Heria')


def set_new_duration_times():
    Workout.objects.filter(instructor='John Smith').update(duration='15 minutes')
    Workout.objects.filter(instructor='Sarah Davis').update(duration='30 minutes')
    Workout.objects.filter(instructor='Chris Heria').update(duration='45 minutes')
    Workout.objects.filter(instructor='Michael Williams').update(duration='1 hour')
    Workout.objects.filter(instructor='Emily Johnson').update(duration='1 hour and 30 minutes')


def delete_workouts():
    Workout.objects.exclude(workout_type__in=(WorkoutChoices.STRENGTH, WorkoutChoices.CALISTHENICS)).delete()




# Run and print your queries


