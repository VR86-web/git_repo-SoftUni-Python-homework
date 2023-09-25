x = float(input())
y = float(input())
h = float(input())

left_side_wall = x * y
right_side_wall = x * y
window = 2.25
back_side_wall = x * x
front_wall = x * x
door = 2.4
total_walls_area = left_side_wall \
                   + right_side_wall \
                   + back_side_wall \
                   + front_wall \
                   - 6.90
back_and_front_roof_side = 2 * (x * y)
side_roof_sides = 2 * (x * h / 2)
total_roof_area = back_and_front_roof_side + side_roof_sides
green_paint = total_walls_area / 3.4
red_paint = total_roof_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")



