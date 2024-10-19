n = int(input())
fishing_area = [list(input()) for _ in range(n)]

# Finding the initial position of the ship
ship_row, ship_col = -1, -1
for i in range(n):
    for j in range(n):
        if fishing_area[i][j] == "S":
            ship_row, ship_col = i, j
            break
    if ship_row != -1:
        break

fish_caught = 0
quota = 20

game_over = False

while True:
    command = input()
    if command == "collect the nets" or game_over:
        break

    if command == "up":
        new_row, new_col = (ship_row - 1) % n, ship_col
    elif command == "down":
        new_row, new_col = (ship_row + 1) % n, ship_col
    elif command == "left":
        new_row, new_col = ship_row, (ship_col - 1) % n
    elif command == "right":
        new_row, new_col = ship_row, (ship_col + 1) % n
    else:
        continue

    # Check if the new position is a whirlpool
    if fishing_area[new_row][new_col] == "W":
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_row},{new_col}]"
        )
        game_over = True
        break

    # Move the ship to the new position
    if fishing_area[new_row][new_col].isdigit():
        fish_caught += int(fishing_area[new_row][new_col])
        fishing_area[new_row][new_col] = "-"

    fishing_area[ship_row][ship_col] = "-"
    ship_row, ship_col = new_row, new_col
    fishing_area[ship_row][ship_col] = "S"

if not game_over:
    if fish_caught >= quota:
        print("Success! You managed to reach the quota!")
    else:
        print(
            f"You didn't catch enough fish and didn't reach the quota! You need {quota - fish_caught} tons of fish more."
        )

    if fish_caught > 0:
        print(f"Amount of fish caught: {fish_caught} tons.")

    # Print the final state of the fishing area
    for row in fishing_area:
        print("".join(row))
