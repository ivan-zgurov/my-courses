n = int(input())
board = [list(input()) for _ in range(n)]

# Finding the initial position of the gambler
gambler_row, gambler_col = -1, -1
for i in range(n):
    for j in range(n):
        if board[i][j] == "G":
            gambler_row, gambler_col = i, j
            break
    if gambler_row != -1:
        break

gambler_amount = 100

game_over = False

while True:
    command = input()
    if command == "end" or game_over:
        break

    if command == "up":
        new_row, new_col = gambler_row - 1, gambler_col
    elif command == "down":
        new_row, new_col = gambler_row + 1, gambler_col
    elif command == "left":
        new_row, new_col = gambler_row, gambler_col - 1
    elif command == "right":
        new_row, new_col = gambler_row, gambler_col + 1
    else:
        continue

    # Check if the gambler leaves the board boundaries
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        print("Game over! You lost everything!")
        game_over = True
        break

    # Move the gambler to the new position
    if board[new_row][new_col] == "W":
        gambler_amount += 100
    elif board[new_row][new_col] == "P":
        gambler_amount -= 200
    elif board[new_row][new_col] == "J":
        gambler_amount += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {gambler_amount}$")
        board[gambler_row][gambler_col] = "-"
        board[new_row][new_col] = "G"
        game_over = True
        break

    if gambler_amount <= 0:
        print("Game over! You lost everything!")
        game_over = True
        break

    board[gambler_row][gambler_col] = "-"
    gambler_row, gambler_col = new_row, new_col
    board[gambler_row][gambler_col] = "G"

if not game_over:
    print(f"End of the game. Total amount: {gambler_amount}$")
    for row in board:
        print("".join(row))
