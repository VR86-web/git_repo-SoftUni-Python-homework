# Generated by Django 5.0.4 on 2024-06-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
