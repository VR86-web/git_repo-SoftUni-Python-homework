from collections import deque


def perfect_fireworks():
    if fireworks_type["Palm Fireworks"] >= 3 \
            and fireworks_type["Willow Fireworks"] >= 3 and \
            fireworks_type["Crossette Fireworks"] >= 3:
        return True


firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = deque(int(x) for x in input().split(", "))

fireworks_type = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

time_to_shine = False

while firework_effects and explosive_power:
    effect = firework_effects.popleft()
    if effect <= 0:
        continue

    power = explosive_power.pop()
    if power <= 0:
        firework_effects.appendleft(effect)
        continue

    current_sum = effect + power

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        fireworks_type["Palm Fireworks"] += 1

    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        fireworks_type["Willow Fireworks"] += 1

    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks_type["Crossette Fireworks"] += 1

    else:
        effect -= 1
        firework_effects.append(effect)
        explosive_power.append(power)

    if perfect_fireworks():
        time_to_shine = True
        print("Congrats! You made the perfect firework show!")
        break

if not time_to_shine:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f" Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in fireworks_type.items():
    print(f"{key}: {value}")


