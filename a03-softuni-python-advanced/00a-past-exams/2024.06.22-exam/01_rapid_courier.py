# 87/ 100

packages = list(map(int, input().split()))
couriers = list(map(int, input().split()))

total_weight = 0

while packages and couriers:
    current_package = packages.pop()  # Take last package
    current_courier = couriers.pop(0)  # Take first courier

    if current_courier >= current_package:
        total_weight += current_package
        remaining_capacity = current_courier - 2 * current_package
        if remaining_capacity > 0:
            couriers.append(remaining_capacity)
    else:
        total_weight += current_courier
        current_package -= current_courier
        packages.insert(0, current_package)

if not packages and not couriers:
    print(f"Total weight: {total_weight} kg")
    print(
        "Congratulations, all packages were delivered successfully by the couriers today."
    )
elif packages and not couriers:
    print(f"Total weight: {total_weight} kg")
    print(
        "Unfortunately, there are no more available couriers to deliver the following packages: "
        + ", ".join(map(str, packages))
    )
elif couriers and not packages:
    print(f"Total weight: {total_weight} kg")
    print(
        "Couriers are still on duty: "
        + ", ".join(map(str, couriers))
        + " but there are no more packages to deliver."
    )
