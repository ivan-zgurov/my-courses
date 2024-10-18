# 62 / 100
armor = list(map(int, input().split(",")))
strikes = list(map(int, input().split(",")))

killed_monsters = 0

while armor and strikes:
    current_armor = armor.pop(0)  # Queue behavior (FIFO)
    current_strike = strikes.pop()  # Stack behavior (LIFO)

    if current_strike >= current_armor:
        killed_monsters += 1
        remaining_strike = current_strike - current_armor
        if remaining_strike > 0 and strikes:
            strikes[-1] += remaining_strike
        elif remaining_strike > 0:
            strikes.append(remaining_strike)
    else:
        current_armor -= current_strike
        armor.append(current_armor)

if not armor:
    print("All monsters have been killed!")
else:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
