amount_chicken_menus = int(input())
amount_fish_menus = int(input())
amount_veggie_menus = int(input())

sum_chicken_menus = amount_chicken_menus * 10.35
sum_fish_menus = amount_fish_menus * 12.40
sum_veggie_menus = amount_veggie_menus * 8.15
sum_dessert = (sum_chicken_menus + sum_fish_menus + sum_veggie_menus) * 0.2
sum_delivery = 2.5

total_sum = sum_chicken_menus + sum_fish_menus + sum_veggie_menus + sum_dessert + sum_delivery
print(total_sum)
