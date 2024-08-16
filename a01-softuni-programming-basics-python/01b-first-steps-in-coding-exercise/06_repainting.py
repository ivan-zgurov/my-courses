amount_needed_plastic = int(input())
amount_needed_paint = int(input())
amount_needed_paint_thinner = int(input())
amount_needed_work_hours = int(input())

sum_plastic = amount_needed_plastic + 2
sum_paint = amount_needed_paint + amount_needed_paint * 0.1
sum_bags = 0.4
sum_materials = sum_plastic * 1.5 + sum_paint * 14.5 + amount_needed_paint_thinner * 5 + sum_bags
sum_work = amount_needed_work_hours * sum_materials * 0.3

total_sum = sum_materials + sum_work

print(total_sum)
