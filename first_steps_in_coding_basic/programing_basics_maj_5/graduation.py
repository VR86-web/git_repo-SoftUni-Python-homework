name_of_student = input()
grades_counter = 0
years_counter = 0
failed_years = 0
while True:
    grade = float(input())

    if grade < 4:
        failed_years += 1
        if failed_years > 1:
            print(f"{name_of_student} has been excluded at {years_counter + 1} grade")
            break
        continue

    else:
        grades_counter += grade
    years_counter += 1

    if years_counter == 12:
        break
if failed_years < 2:
    average_grade = grades_counter / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")


