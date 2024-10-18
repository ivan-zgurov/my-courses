def cookbook(*recipes):
    cuisine_dict = {}

    # Organize recipes by cuisine
    for recipe_name, cuisine, ingredients in recipes:
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((recipe_name, ingredients))

    # Sort cuisines
    sorted_cuisines = sorted(cuisine_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    # Sort recipes
    result = []
    for cuisine, recipes_list in sorted_cuisines:
        recipes_list.sort(key=lambda x: x[0])
        result.append(f"{cuisine} cuisine contains {len(recipes_list)} recipes:")
        for recipe_name, ingredients in recipes_list:
            ingredients_str = ", ".join(ingredients)
            result.append(f"  * {recipe_name} -> Ingredients: {ingredients_str}")

    return "\n".join(result)


# Examples
print(
    cookbook(
        (
            "Spaghetti Bolognese",
            "Italian",
            ["spaghetti", "tomato sauce", "ground beef"],
        ),
        ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
        ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
        ("Croissant", "French", ["flour", "butter", "yeast"]),
        ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    )
)

print(
    cookbook(
        (
            "Pad Thai",
            "Thai",
            ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"],
        )
    )
)

print(
    cookbook(
        (
            "Spaghetti Bolognese",
            "Italian",
            ["spaghetti", "tomato sauce", "ground beef"],
        ),
        ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
        ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
        ("Croissant", "French", ["flour", "butter", "yeast"]),
        ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
        ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
        ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
        ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"]),
    )
)
