def plant_garden(available_space, *allowed_plants, **plant_requests):
    allowed_plants_dict = {plant: space for plant, space in allowed_plants}

    sorted_requests = sorted(plant_requests.items())

    planted_plants = {}

    for plant, requested_quantity in sorted_requests:
        if plant in allowed_plants_dict:
            space_per_plant = allowed_plants_dict[plant]
            max_plantable = int(available_space // space_per_plant)

            if max_plantable > 0:
                plantable_quantity = min(requested_quantity, max_plantable)
                planted_plants[plant] = plantable_quantity

                available_space -= plantable_quantity * space_per_plant

                if available_space < min(allowed_plants_dict.values()):
                    break

    all_planted = all(
        plant in planted_plants and planted_plants[plant] == quantity
        for plant, quantity in plant_requests.items()
        if plant in allowed_plants_dict
    )

    if all_planted:
        result = f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n"
        result += "Planted plants:\n"
        result += "\n".join(f"{plant}: {quantity}" for plant, quantity in sorted(planted_plants.items()))
    else:
        result = "Not enough space to plant all requested plants!\n"
        result += "Planted plants:\n"
        result += "\n".join(f"{plant}: {quantity}" for plant, quantity in sorted(planted_plants.items()))

    return result

