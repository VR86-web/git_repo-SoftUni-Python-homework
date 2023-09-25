country = input()
device = input()
difficulty_points_counter = 0
performance_points_counter = 0
if country == "Russia":
    if device == "ribbon":
        difficulty_points_counter += 9.100
        performance_points_counter += 9.400
    elif device == "hoop":
        difficulty_points_counter += 9.300
        performance_points_counter += 9.800
    elif device == "rope":
        difficulty_points_counter += 9.600
        performance_points_counter += 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        difficulty_points_counter += 9.600
        performance_points_counter += 9.400
    elif device == "hoop":
        difficulty_points_counter += 9.550
        performance_points_counter += 9.750
    elif device == "rope":
        difficulty_points_counter += 9.500
        performance_points_counter += 9.400
elif country == "Italy":
    if device == "ribbon":
        difficulty_points_counter += 9.200
        performance_points_counter += 9.500
    elif device == "hoop":
        difficulty_points_counter += 9.450
        performance_points_counter += 9.350
    elif device == "rope":
        difficulty_points_counter += 9.700
        performance_points_counter += 9.150
total_points = difficulty_points_counter + performance_points_counter
points_needed = 20 - total_points
percentage_needed_points = (points_needed / 20) * 100
print(f"The team of {country} get {total_points:.3f} on {device}.")
print(f"{percentage_needed_points:.2f}%")
