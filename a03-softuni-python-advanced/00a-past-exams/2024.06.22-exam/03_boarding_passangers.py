def boarding_passengers(ship_capacity, *passenger_groups):
    boarded_passengers = {}
    remaining_capacity = ship_capacity

    for num_passengers, benefit_program in passenger_groups:
        if remaining_capacity == 0:
            break

        if num_passengers <= remaining_capacity:
            remaining_capacity -= num_passengers
            if benefit_program in boarded_passengers:
                boarded_passengers[benefit_program] += num_passengers
            else:
                boarded_passengers[benefit_program] = num_passengers

    # Sort the boarding details
    sorted_boarding_details = sorted(
        boarded_passengers.items(), key=lambda x: (-x[1], x[0])
    )

    # Output
    result = ["Boarding details by benefit plan:"]
    for benefit_program, total_passengers in sorted_boarding_details:
        result.append(f"## {benefit_program}: {total_passengers} guests")

    if remaining_capacity == 0 and sum(boarded_passengers.values()) < sum(
        group[0] for group in passenger_groups
    ):
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif remaining_capacity > 0 and sum(boarded_passengers.values()) < sum(
        group[0] for group in passenger_groups
    ):
        result.append(
            f"Partial boarding completed. Available capacity: {remaining_capacity}."
        )
    else:
        result.append("All passengers are successfully boarded!")

    return "\n".join(result)


# Examples
print(
    boarding_passengers(
        150, (35, "Diamond"), (55, "Platinum"), (35, "Gold"), (25, "First Cruiser")
    )
)
print(
    boarding_passengers(
        100,
        (20, "Diamond"),
        (15, "Platinum"),
        (25, "Gold"),
        (25, "First Cruiser"),
        (15, "Diamond"),
        (10, "Gold"),
    )
)
print(
    boarding_passengers(
        120,
        (30, "Gold"),
        (20, "Platinum"),
        (30, "Diamond"),
        (10, "First Cruiser"),
        (31, "Platinum"),
        (20, "Diamond"),
    )
)
