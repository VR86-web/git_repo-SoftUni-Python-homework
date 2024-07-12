from django.db import models


class MealTypeChoices(models.TextChoices):
    BREAKFAST = 'Breakfast', 'Breakfast'
    LUNCH = 'Lunch', 'Lunch'
    DINNER = 'Dinner', 'Dinner'
    SNACK = 'Snack', 'Snack'


class DungeonChoices(models.TextChoices):
    EASY = 'Easy', 'Easy'
    MEDIUM = 'Medium', 'Medium'
    HARD = 'Hard', 'Hard'


class WorkoutChoices(models.TextChoices):
    CARDIO = 'Cardio', 'Cardio'
    STRENGTH = 'Strength', 'Strength'
    YOGA = 'Yoga', 'Yoga'
    CROSSFIT = 'CrossFit', 'CrossFit'
    CALISTHENICS = 'Calisthenics', 'Calisthenics'


