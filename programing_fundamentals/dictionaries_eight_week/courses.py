courses_dict = {}
command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_dict.keys():
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name] += [student_name]
    command = input()
for course, students in courses_dict.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")