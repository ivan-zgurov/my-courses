planned_budget = float(input())
amount_vgas = int(input())
amount_cpus = int(input())
amount_ram = int(input())

total_price_vgas = amount_vgas * 250
total_price_cpus = amount_cpus * total_price_vgas * 0.35
total_price_ram = amount_ram * total_price_vgas * 0.1

total_price_sum = total_price_vgas + total_price_cpus + total_price_ram

if amount_vgas > amount_cpus:
    total_price_sum *= 0.85

if planned_budget < total_price_sum:
    print(f"Not enough money! You need {total_price_sum - planned_budget:.02f} leva more!")

else:
    print(f"You have {planned_budget - total_price_sum:.02f} leva left!")
