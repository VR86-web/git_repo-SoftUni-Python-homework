def bee_eater_battle(bees, bee_eaters):
    bees = list(map(int, bees.split()))
    bee_eaters = list(map(int, bee_eaters.split()))

    while bees and bee_eaters:
        bees_group = bees.pop(0)
        bee_eaters_group = bee_eaters.pop()

        while bees_group > 0 and bee_eaters_group > 0:
            bees_group -= bee_eaters_group * 7
            bee_eaters_group -= (bee_eaters_group * 7 > bees_group)

        if bees_group > 0:
            bees.insert(0, bees_group)
        else:
            bee_eaters.insert(0, bee_eaters_group)

    return bees, bee_eaters


def print_results(bees, bee_eaters):
    print("The final battle is over!")
    if not bees and not bee_eaters:
        print("But no one made it out alive!")
    elif bees:
        print(f"Bee groups left: {', '.join(map(str, bees))}")
    elif bee_eaters:
        print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")


bees = input()
bee_eaters = input()

result = bee_eater_battle(bees, bee_eaters)
print_results(*result)