import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student


def add_students():
    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )

    Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )


def get_students_info():
    info_list = []
    for student in Student.objects.all():
        info_list.append(f"Student №{student.student_id}: {student.first_name} {student.last_name}; "
                         f"Email: {student.email}")

    return '\n'.join(info_list)


def update_students_emails():
    all_students = Student.objects.all()
    for s in all_students:
        s.email = s.email.replace(s.email.split('@')[1], "uni-students.com")
        s.save()


def truncate_students():
    all_students = Student.objects.all().delete()
# Run and print your queries



