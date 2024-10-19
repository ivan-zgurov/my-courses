n, m = map(int, input().split(","))
cupboard = [list(input()) for _ in range(n)]

# Finding the initial position of the mouse
mouse_row, mouse_col = -1, -1
for i in range(n):
    for j in range(m):
        if cupboard[i][j] == "M":
            mouse_row, mouse_col = i, j
            break
    if mouse_row != -1:
        break

cheese_count = sum(row.count("C") for row in cupboard)

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    if command == "up":
        new_row, new_col = mouse_row - 1, mouse_col
    elif command == "down":
        new_row, new_col = mouse_row + 1, mouse_col
    elif command == "left":
        new_row, new_col = mouse_row, mouse_col - 1
    elif command == "right":
        new_row, new_col = mouse_row, mouse_col + 1
    else:
        continue

    # Check if the mouse steps outside the cupboard
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
        print("No more cheese for tonight!")
        break

    # Check if the new position is a wall
    if cupboard[new_row][new_col] == "@":
        continue

    # Move the mouse to the new position
    if cupboard[new_row][new_col] == "C":
        cheese_count -= 1
        if cheese_count == 0:
            cupboard[mouse_row][mouse_col] = "*"
            mouse_row, mouse_col = new_row, new_col
            cupboard[mouse_row][mouse_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif cupboard[new_row][new_col] == "T":
        cupboard[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = new_row, new_col
        cupboard[mouse_row][mouse_col] = "M"
        print("Mouse is trapped!")
        break

    cupboard[mouse_row][mouse_col] = "*"
    mouse_row, mouse_col = new_row, new_col
    cupboard[mouse_row][mouse_col] = "M"

# Print the final state of the cupboard
for row in cupboard:
    print("".join(row))
