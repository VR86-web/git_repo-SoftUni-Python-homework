import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
from django.db.models import Q, Count, Sum, Avg


# Create queries within functions


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    astronaut = Astronaut.objects.filter(
        Q(name__icontains=search_string)
            |
        Q(phone_number__icontains=search_string)
    ).order_by('name')

    if not astronaut.exists():
        return ''

    result = []
    for a in astronaut:
        status = "Active" if a.is_active else "Inactive"
        result.append(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut():
    top_astronauts = Astronaut.objects.annotate(num_of_missions=Count('mission')).order_by(
        '-num_of_missions', 'phone_number')

    if not top_astronauts.exists() or top_astronauts.first().num_of_missions == 0:
        return "No data."

    top_astronaut = top_astronauts.first()

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.num_of_missions} missions."


def get_top_commander():
    astronauts = Astronaut.objects.annotate(num_of_commanded_missions=Count('missions_as_commander')).order_by(
        '-num_of_commanded_missions', 'phone_number')

    if not astronauts.exists() or astronauts.first().num_of_commanded_missions == 0:
        return "No data."

    top_commander = astronauts.first()

    return f"Top Commander: {top_commander.name} with {top_commander.num_of_commanded_missions} commanded missions."


def get_last_completed_mission():
    last_completed_mission = Mission.objects.filter(
        status='Completed',
    ).order_by('-launch_date').first()

    if not last_completed_mission:
        return "No data."

    commander = last_completed_mission.commander.name if last_completed_mission.commander else 'TBA'

    astronauts = last_completed_mission.astronauts.order_by('name')

    astronaut = ', '.join([a.name for a in astronauts])

    spacecraft = last_completed_mission.spacecraft.name

    total_spacewalks = sum(a.spacewalks for a in last_completed_mission.astronauts.all())

    result = (
        f"The last completed mission is: {last_completed_mission.name}. "
        f"Commander: {commander}. "
        f"Astronauts: {astronaut}. "
        f"Spacecraft: {spacecraft}. "
        f"Total spacewalks: {total_spacewalks}."
    )

    return result


def get_most_used_spacecraft():
    most_used_spacecrafts = Spacecraft.objects.annotate(missions_count=Count('mission')).order_by(
        '-missions_count', 'name').first()

    if not most_used_spacecrafts.exists() or most_used_spacecrafts.num_missions == 0:
        return "No data."

    num_astronauts = most_used_spacecrafts.mission_set.all().values_list('astronauts', flat=True).distinct().count()

    return (f"The most used spacecraft is: {most_used_spacecrafts.name}, "
            f"manufactured by {most_used_spacecrafts.manufacturer}, "
            f"used in {most_used_spacecrafts.mission_count} missions, astronauts on missions: {num_astronauts}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(mission__status='Planned').distinct()
    affected_spacecrafts = 0
    total_spacecraft_weight = 0

    for spacecraft in spacecrafts:
        if spacecraft.weight >= 200.0:
            spacecraft.weight -= 200.0
            spacecraft.save()
            affected_spacecrafts += 1
            total_spacecraft_weight += spacecraft.weight

    if affected_spacecrafts == 0:
        return "No changes in weight."

    average_weight = Spacecraft.objects.aggregate(Avg('weight'))['weight__avg']
    return (f"The weight of {affected_spacecrafts} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {average_weight:.1f}kg")

