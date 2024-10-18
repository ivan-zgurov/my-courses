# 70 / 100

bees = list(map(int, input().split()))
bee_eaters = list(map(int, input().split()))

while bees and bee_eaters:
    current_bees = bees.pop(0)
    current_bee_eaters = bee_eaters.pop()
    while current_bees > 0 and current_bee_eaters > 0:
        if current_bee_eaters * 7 >= current_bees:
            bees_killed = min(current_bees, current_bee_eaters * 7)
            current_bees -= bees_killed
            current_bee_eaters -= bees_killed // 7

            if current_bees == 0:
                if current_bee_eaters > 0:
                    bee_eaters.insert(0, current_bee_eaters)
                break
        else:
            bees_killed = current_bee_eaters * 7
            current_bees -= bees_killed
            current_bee_eaters = 0
            if current_bee_eaters == 0:
                if current_bees > 0:
                    bees.append(current_bees)

print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")
