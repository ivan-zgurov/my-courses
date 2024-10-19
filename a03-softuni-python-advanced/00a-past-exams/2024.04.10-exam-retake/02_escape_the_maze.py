n = int(input())
maze = [list(input()) for _ in range(n)]

# Finding the initial position of the traveller
traveller_row, traveller_col = -1, -1
for i in range(n):
    for j in range(n):
        if maze[i][j] == "P":
            traveller_row, traveller_col = i, j
            break
    if traveller_row != -1:
        break

health = 100

while True:
    command = input()
    if health <= 0:
        break

    if command == "up":
        new_row, new_col = traveller_row - 1, traveller_col
    elif command == "down":
        new_row, new_col = traveller_row + 1, traveller_col
    elif command == "left":
        new_row, new_col = traveller_row, traveller_col - 1
    elif command == "right":
        new_row, new_col = traveller_row, traveller_col + 1
    else:
        continue

    # Check if the traveller moves within boundaries
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        continue

    # Move the traveller to the new position
    if maze[new_row][new_col] == "M":
        health -= 40
        if health <= 0:
            health = 0  # Ensure health does not go below 0
            maze[traveller_row][traveller_col] = "-"
            maze[new_row][new_col] = "P"
            print("Player is dead. Maze over!")
            break
        else:
            maze[new_row][new_col] = "-"
    elif maze[new_row][new_col] == "H":
        health = min(100, health + 15)
        maze[new_row][new_col] = "-"
    elif maze[new_row][new_col] == "X":
        maze[traveller_row][traveller_col] = "-"
        maze[new_row][new_col] = "P"
        print("Player escaped the maze. Danger passed!")
        break

    maze[traveller_row][traveller_col] = "-"
    traveller_row, traveller_col = new_row, new_col
    maze[traveller_row][traveller_col] = "P"

# Print the final state of the maze
print(f"Player's health: {health} units")
for row in maze:
    print("".join(row))
