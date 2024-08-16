amount_dog_food_packages = int(input())
amount_cat_food_packages = int(input())

costs_dog_food = 2.5 * amount_dog_food_packages
costs_cat_food = 4.0 * amount_cat_food_packages
costs_total = costs_cat_food + costs_dog_food

print(f"{costs_total} lv.")
