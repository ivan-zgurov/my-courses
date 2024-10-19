n = int(input())
field = [list(input()) for _ in range(n)]

# Finding the initial position of the bee
bee_row, bee_col = -1, -1
for i in range(n):
    for j in range(n):
        if field[i][j] == "B":
            bee_row, bee_col = i, j
            break
    if bee_row != -1:
        break

energy = 15
nectar_collected = 0
energy_restored = False

while True:
    command = input()
    if energy <= 0:
        break

    if command == "up":
        new_row, new_col = (bee_row - 1) % n, bee_col
    elif command == "down":
        new_row, new_col = (bee_row + 1) % n, bee_col
    elif command == "left":
        new_row, new_col = bee_row, (bee_col - 1) % n
    elif command == "right":
        new_row, new_col = bee_row, (bee_col + 1) % n
    else:
        continue

    energy -= 1

    # Move the bee to the new position
    if energy == 0:
        if nectar_collected >= 30 and not energy_restored:
            energy = nectar_collected - 30
            nectar_collected = 30
            energy_restored = True
        else:
            print("This is the end! Beesy ran out of energy.")
            field[bee_row][bee_col] = "-"
            field[new_row][new_col] = "B"
            break

    if field[new_row][new_col].isdigit():
        nectar_collected += int(field[new_row][new_col])
        field[new_row][new_col] = "-"
    elif field[new_row][new_col] == "H":
        field[bee_row][bee_col] = "-"
        field[new_row][new_col] = "B"
        if nectar_collected >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    field[bee_row][bee_col] = "-"
    bee_row, bee_col = new_row, new_col
    field[bee_row][bee_col] = "B"

# Print the final state of the field
for row in field:
    print("".join(row))
