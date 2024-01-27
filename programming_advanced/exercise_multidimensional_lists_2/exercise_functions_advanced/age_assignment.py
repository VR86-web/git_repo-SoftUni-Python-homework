def age_assignment(*names, **names_data):
    result = []

    for key, value in names_data.items():
        for name in names:
            if name.startswith(key):
                result.append(f"{name} is {value} years old.")
                break

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))