def cookbook(*recipes):
    cuisines = {}

    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisines.keys():
            cuisines[cuisine] = []
        cuisines[cuisine].append((name, ingredients))

    output = []

    for cuisine in sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{cuisine[0]} cuisine contains {len(cuisine[1])} recipes:")

        for recipe in sorted(cuisine[1], key=lambda x: x[0]):
            output.append(f"  *{recipe[0]} -> Ingredients: {', '.join(recipe[1])}")

    return "\n".join(output)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))