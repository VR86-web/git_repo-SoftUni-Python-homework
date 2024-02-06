from collections import deque


def check_range(cur_sum):
    if 100 <= cur_sum < 500:
        return True
    return False


def check_cur_sum(cur_sum):
    if 100 <= cur_sum < 200:
        gifts["Gemstone"] += 1
    elif 200 <= cur_sum < 300:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= cur_sum < 400:
        gifts["Gold"] += 1
    elif 400 <= cur_sum < 500:
        gifts["Diamond Jewellery"] += 1


materials_for_wedding = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}


while materials_for_wedding and magic_level:
    material = materials_for_wedding.pop()
    magic = magic_level.popleft()
    current_sum = material + magic

    if check_range(current_sum):
        check_cur_sum(current_sum)

    elif current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = material * 2 + magic * 3
        else:
            current_sum *= 2

        if check_range(current_sum):
            check_cur_sum(current_sum)

    elif current_sum >= 500:
        current_sum /= 2
        if check_range(current_sum):
            check_cur_sum(current_sum)


if (gifts["Gemstone"] and gifts["Porcelain Sculpture"]) \
        or (gifts["Gold"] and gifts["Diamond Jewellery"]):
    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")

if materials_for_wedding:
    print(f"Materials left: {', '.join([str(x) for x in materials_for_wedding])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

sorted_gifts = sorted(gifts.items(), key=lambda x: x[0])

for key, value in sorted_gifts:
    if value > 0:
        print(f"{key}: {value}")
