box_of_clothes = [int(x) for x in input().split()]
capacity_of_single_rack = int(input())

racks_count = 1
current_rack_space = capacity_of_single_rack
while box_of_clothes:
    cloth = box_of_clothes.pop()
    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = capacity_of_single_rack - cloth

print(racks_count)
