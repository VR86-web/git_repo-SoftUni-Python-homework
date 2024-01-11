employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())
employee_total = employee1_efficiency + employee2_efficiency + employee3_efficiency
hours = 0
while students_count > 0:
    students_count -= employee_total
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")
