size = int(input())
commands = input().split(", ")
field = [list(input()) for _ in range(size)]

# Finding the initial position of the squirrel
for i in range(size):
    for j in range(size):
        if field[i][j] == "s":
            s_row, s_col = i, j
            break

hazelnuts_collected = 0

for command in commands:
    if command == "up":
        s_row -= 1
    elif command == "down":
        s_row += 1
    elif command == "left":
        s_col -= 1
    elif command == "right":
        s_col += 1

    # Check if the squirrel is out of the field
    if s_row < 0 or s_row >= size or s_col < 0 or s_col >= size:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnuts_collected}")
        break

    # Check the current position
    if field[s_row][s_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts_collected}")
        break
    elif field[s_row][s_col] == "h":
        hazelnuts_collected += 1
        field[s_row][s_col] = "*"
        if hazelnuts_collected == 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {hazelnuts_collected}")
            break
else:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts_collected}")
