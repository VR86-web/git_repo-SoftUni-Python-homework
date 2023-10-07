fire = input().split("#")
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []
print("Cells:")
for cell in fire:
    fire_cells = cell.split(" = ")
    type_of_fire = fire_cells[0]
    cells = int(fire_cells[1])
    valid = False
    if type_of_fire == "High":
        if 81 <= cells <= 125:
            valid = True
    if type_of_fire == "Medium":
        if 51 <= cells <= 80:
            valid = True
    if type_of_fire == "Low":
        if 1 <= cells <= 50:
            valid = True
    if water < cells:
        continue
    if valid:
        put_out_cells.append(cells)
        water -= cells
        effort += cells * 0.25
        total_fire += cells
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
