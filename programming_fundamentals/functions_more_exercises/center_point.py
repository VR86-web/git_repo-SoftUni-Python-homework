from math import floor
current_x1, current_y1, current_x2, current_y2 = float(input()), float(input()), float(input()), float(input())


def center_point(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


distance_from_x1_and_y1 = center_point(current_x1, current_y1, 0, 0)
distance_from_x2_and_y2 = center_point(current_x2, current_y2, 0, 0)

if distance_from_x1_and_y1 > distance_from_x2_and_y2:
    print(tuple([floor(current_x2), floor(current_y2)]))
else:
    print(tuple([floor(current_x1), floor(current_y1)]))