student_dict = {}
number_of_pair_rows = int(input())
for rows in range(number_of_pair_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in student_dict:
        student_dict[student_name] = []
    student_dict[student_name].append(student_grade)
filtered_students = {}
for student, grade in student_dict.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        filtered_students[student] = average_grade
for name, grade in filtered_students.items():
    print(f"{name} -> {grade:.2f}")
