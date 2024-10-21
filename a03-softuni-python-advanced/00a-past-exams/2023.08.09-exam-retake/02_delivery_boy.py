n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

# Finding the initial position of the delivery boy
boy_row, boy_col = -1, -1
for i in range(n):
    for j in range(m):
        if field[i][j] == "B":
            boy_row, boy_col = i, j
            break
    if boy_row != -1:
        break

pizza_collected = False

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    if command == "up":
        new_row, new_col = boy_row - 1, boy_col
    elif command == "down":
        new_row, new_col = boy_row + 1, boy_col
    elif command == "left":
        new_row, new_col = boy_row, boy_col - 1
    elif command == "right":
        new_row, new_col = boy_row, boy_col + 1
    else:
        continue

    # Check if the delivery boy steps outside the field
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
        print("The delivery is late. Order is canceled.")
        field[boy_row][boy_col] = " "
        break

    # Check if the new position is an obstacle
    if field[new_row][new_col] == "*":
        continue

    # Move the delivery boy to the new position
    if field[new_row][new_col] == "P" and not pizza_collected:
        pizza_collected = True
        field[new_row][new_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
    elif field[new_row][new_col] == "A" and pizza_collected:
        field[new_row][new_col] = "P"
        print("Pizza is delivered on time! Next order...")
        field[boy_row][boy_col] = "."
        boy_row, boy_col = new_row, new_col
        break

    # Mark the road as part of the path
    if field[boy_row][boy_col] != "B":
        field[boy_row][boy_col] = "."
    boy_row, boy_col = new_row, new_col
    field[boy_row][boy_col] = "B"

# Print the final state of the field
for row in field:
    print("".join(row))
