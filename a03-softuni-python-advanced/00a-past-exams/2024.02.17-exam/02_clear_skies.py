n = int(input())
airspace = [list(input()) for _ in range(n)]

# Finding the initial position of the jetfighter
jetfighter_row, jetfighter_col = -1, -1
for i in range(n):
    for j in range(n):
        if airspace[i][j] == "J":
            jetfighter_row, jetfighter_col = i, j
            break
    if jetfighter_row != -1:
        break

armor = 300
enemy_count = sum(row.count("E") for row in airspace)

while True:
    command = input()
    if enemy_count == 0 or armor <= 0:
        break

    if command == "up":
        new_row, new_col = jetfighter_row - 1, jetfighter_col
    elif command == "down":
        new_row, new_col = jetfighter_row + 1, jetfighter_col
    elif command == "left":
        new_row, new_col = jetfighter_row, jetfighter_col - 1
    elif command == "right":
        new_row, new_col = jetfighter_row, jetfighter_col + 1
    else:
        continue

    # Check if the jetfighter moves within boundaries
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        continue

    # Move the jetfighter to the new position
    if airspace[new_row][new_col] == "E":
        enemy_count -= 1
        armor -= 100
        airspace[new_row][new_col] = "-"
        if enemy_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            airspace[jetfighter_row][jetfighter_col] = "-"
            airspace[new_row][new_col] = "J"
            break
        elif armor <= 0:
            print(
                f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!"
            )
            airspace[jetfighter_row][jetfighter_col] = "-"
            airspace[new_row][new_col] = "J"
            break
    elif airspace[new_row][new_col] == "R":
        armor = 300
        airspace[new_row][new_col] = "-"

    airspace[jetfighter_row][jetfighter_col] = "-"
    jetfighter_row, jetfighter_col = new_row, new_col
    airspace[jetfighter_row][jetfighter_col] = "J"

# Print the final state of the airspace
for row in airspace:
    print("".join(row))
