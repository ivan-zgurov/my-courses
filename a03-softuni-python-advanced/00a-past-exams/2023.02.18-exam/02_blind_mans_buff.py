n, m = map(int, input().split())
playground = [input().split() for _ in range(n)]

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

# Finding the initial position of 'B'
for i in range(n):
    for j in range(m):
        if playground[i][j] == "B":
            b_row, b_col = i, j
            break

moves_made = 0
touched_opponents = 0

while True:
    command = input()
    if command == "Finish":
        break

    if command in directions:
        new_row = b_row + directions[command][0]
        new_col = b_col + directions[command][1]

        # Check if the new position is within bounds
        if 0 <= new_row < n and 0 <= new_col < m:
            # Check if the new position is not an obstacle
            if playground[new_row][new_col] != "O":
                # Update moves_made if moving to an empty cell or touching an opponent
                moves_made += 1

                # Check if the new position is an opponent
                if playground[new_row][new_col] == "P":
                    touched_opponents += 1
                    playground[new_row][new_col] = "-"

                # Update the position of 'B'
                b_row, b_col = new_row, new_col

    # End the game if all opponents are touched
    if touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
