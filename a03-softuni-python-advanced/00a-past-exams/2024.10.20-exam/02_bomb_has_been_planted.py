def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def play_game(grid, commands):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "C":
                x, y = i, j
                initial_x, initial_y = x, y
                break

    time_remaining = 16
    bomb_defused = False
    counter_terrorist_alive = True

    for command in commands:
        if time_remaining <= 0:
            break

        if command == "up":
            if x > 0:
                x -= 1
        elif command == "down":
            if x < len(grid) - 1:
                x += 1
        elif command == "left":
            if y > 0:
                y -= 1
        elif command == "right":
            if y < len(grid[0]) - 1:
                y += 1
        elif command == "defuse":
            if grid[x][y] == "B":
                time_remaining -= 4
                if time_remaining >= 0:
                    grid[x][y] = "D"
                    bomb_defused = True
                    break
                else:
                    grid[x][y] = "X"
                    counter_terrorist_alive = False
                    break
            else:
                time_remaining -= 2
                continue

        if grid[x][y] == "T":
            grid[x][y] = "*"
            counter_terrorist_alive = False
            break

        time_remaining -= 1

    if bomb_defused:
        print("Counter-terrorist wins!")
        print(f"Bomb has been defused: {abs(time_remaining)} second/s remaining.")

    elif not counter_terrorist_alive:
        print("Terrorists win!")

    elif time_remaining <= 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(time_remaining)} second/s.")

    grid[initial_x][initial_y] = "C"
    print_grid(grid)

rows, cols = map(int, input().split(", "))
grid = [list(input()) for _ in range(rows)]
commands = []
while True:
    try:
        command = input()
        commands.append(command)
    except EOFError:
        break

play_game(grid, commands)