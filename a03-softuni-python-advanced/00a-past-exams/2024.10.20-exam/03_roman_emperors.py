def list_roman_emperors(*emperors, **rule_lengths):
    successful_emperors = []
    unsuccessful_emperors = []

    # Classify emperors by their success status
    for emperor_name, is_successful in emperors:
        rule_length = rule_lengths.get(emperor_name, 0)
        if is_successful:
            successful_emperors.append((emperor_name, rule_length))
        else:
            unsuccessful_emperors.append((emperor_name, rule_length))

    # Sort successful emperors by rule length (descending) and name (ascending)
    successful_emperors.sort(key=lambda x: (-x[1], x[0]))
    # Sort unsuccessful emperors by rule length (ascending) and name (ascending)
    unsuccessful_emperors.sort(key=lambda x: (x[1], x[0]))

    # Prepare the output
    result = [f"Total number of emperors: {len(emperors)}"]
    if successful_emperors:
        result.append("Successful emperors:")
        for emperor_name, rule_length in successful_emperors:
            result.append(f"****{emperor_name}: {rule_length}")
    if unsuccessful_emperors:
        result.append("Unsuccessful emperors:")
        for emperor_name, rule_length in unsuccessful_emperors:
            result.append(f"****{emperor_name}: {rule_length}")

    return "\n".join(result)


# Example usage
print(
    list_roman_emperors(
        ("Augustus", True),
        ("Nero", False),
        Augustus=40,
        Nero=14,
    )
)

print(
    list_roman_emperors(
        ("Augustus", True),
        ("Trajan", True),
        ("Nero", False),
        ("Caligula", False),
        ("Pertinax", False),
        ("Vespasian", True),
        Augustus=40,
        Trajan=19,
        Nero=14,
        Caligula=4,
        Pertinax=4,
        Vespasian=19,
    )
)

print(
    list_roman_emperors(
        ("Augustus", True),
        ("Trajan", True),
        ("Claudius", True),
        Augustus=40,
        Trajan=19,
        Claudius=13,
    )
)
