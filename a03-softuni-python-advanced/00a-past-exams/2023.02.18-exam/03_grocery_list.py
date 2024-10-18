def shop_from_grocery_list(budget, grocery_list, *products):
    purchased_products = set()
    remaining_budget = budget

    for product_name, product_price in products:
        if product_name in grocery_list and product_name not in purchased_products:
            if remaining_budget >= product_price:
                purchased_products.add(product_name)
                remaining_budget -= product_price
            else:
                break

    # Output
    missing_products = set(grocery_list) - purchased_products
    if not missing_products:
        return f"Shopping is successful. Remaining budget: {remaining_budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(sorted(missing_products))}."


# Examples
print(
    shop_from_grocery_list(
        100,
        ["tomato", "cola"],
        ("cola", 5.8),
        ("tomato", 10.0),
        ("tomato", 20.45),
    )
)

print(
    shop_from_grocery_list(
        100,
        ["tomato", "cola", "chips", "meat"],
        ("cola", 5.8),
        ("tomato", 10.0),
        ("meat", 22),
    )
)

print(
    shop_from_grocery_list(
        100,
        ["tomato", "cola", "chips", "meat", "chocolate"],
        ("cola", 15.8),
        ("chocolate", 30),
        ("tomato", 15.85),
        ("chips", 50),
        ("meat", 22.99),
    )
)
