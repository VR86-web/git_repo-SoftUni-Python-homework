def check_employee_happiness():
    employees_happiness = list(map(int, input().split()))
    happiness_factor = int(input())

    improved_happiness = [happiness * happiness_factor for happiness in employees_happiness]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_people = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)
    message = "happy" if happy_people >= total_count / 2 else "not happy"
    result = f"Score: {happy_people}/{total_count}. Employees are {message}!"
    return result


print(check_employee_happiness())

