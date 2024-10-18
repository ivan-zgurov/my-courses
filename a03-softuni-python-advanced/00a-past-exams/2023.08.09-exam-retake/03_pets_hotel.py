## 66 / 100

def accommodate_new_pets(capacity, max_weight, *pets):
    accommodated_pets = {}
    available_capacity = capacity

    for pet_type, pet_weight in pets:
        if available_capacity == 0:
            break
        if pet_weight > max_weight:
            continue

        if pet_type in accommodated_pets:
            accommodated_pets[pet_type] += 1
        else:
            accommodated_pets[pet_type] = 1
        available_capacity -= 1

    # Output
    result = []
    if available_capacity == capacity - len(pets):
        result.append(
            f"All pets are accommodated! Available capacity: {available_capacity}."
        )
    else:
        result.append("You did not manage to accommodate all pets!")

    result.append("Accommodated pets:")
    for pet_type in sorted(accommodated_pets):
        result.append(f"{pet_type}: {accommodated_pets[pet_type]}")

    return "\n".join(result)


# Examples
print(
    accommodate_new_pets(
        10,
        15.0,
        ("cat", 5.8),
        ("dog", 10.0),
    )
)

print(
    accommodate_new_pets(
        10,
        10.0,
        ("cat", 5.8),
        ("dog", 10.5),
        ("parrot", 0.8),
        ("cat", 3.1),
    )
)

print(
    accommodate_new_pets(
        2,
        15.0,
        ("dog", 10.0),
        ("cat", 5.8),
        ("cat", 2.7),
    )
)
