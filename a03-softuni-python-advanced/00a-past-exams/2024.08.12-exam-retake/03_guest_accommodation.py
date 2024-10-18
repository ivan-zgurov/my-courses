def accommodate(*guests, **rooms):
    # Sort the rooms 
    available_rooms = sorted(
        rooms.items(), key=lambda x: (x[1], int(x[0].split("_")[1]))
    )

    accommodations = []
    unaccommodated_guests = 0

    for guest in guests:
        suitable_room_index = -1
        best_capacity_diff = float("inf")
        for i, (room_key, capacity) in enumerate(available_rooms):
            if capacity >= guest:
                capacity_diff = capacity - guest
                if capacity_diff < best_capacity_diff:
                    suitable_room_index = i
                    best_capacity_diff = capacity_diff
                elif capacity_diff == best_capacity_diff:
                    # If capacity difference is the same, choose the room with the smallest room number
                    current_room_number = int(
                        available_rooms[suitable_room_index][0].split("_")[1]
                    )
                    new_room_number = int(room_key.split("_")[1])
                    if new_room_number < current_room_number:
                        suitable_room_index = i

        if suitable_room_index != -1:
            room_key, capacity = available_rooms.pop(suitable_room_index)
            room_number = int(room_key.split("_")[1])
            accommodations.append((room_number, guest))
        else:
            unaccommodated_guests += guest

    # Output
    result = []

    if accommodations:
        result.append(
            f"A total of {len(accommodations)} accommodations were completed!"
        )
        for room_number, guest in sorted(accommodations):
            result.append(f"<Room {room_number} accommodates {guest} guests>")
    else:
        result.append("No accommodations were completed!")

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if available_rooms:
        result.append(f"Empty rooms: {len(available_rooms)}")

    return "\n".join(result)


# Examples
print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
