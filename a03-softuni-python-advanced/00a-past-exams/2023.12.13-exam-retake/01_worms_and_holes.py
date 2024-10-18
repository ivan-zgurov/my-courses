# 75 / 100

worms = list(map(int, input().split()))
holes = list(map(int, input().split()))

matches = 0

while worms and holes:
    current_worm = worms.pop()  # Take last worm
    current_hole = holes.pop(0)  # Take first hole

    if current_worm == current_hole:
        matches += 1
    else:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and matches == len(holes) + matches:
    print("Every worm found a suitable hole!")
elif not worms:
    print("Worms left: none")
else:
    print("Worms left: " + ", ".join(map(str, worms)))

if not holes:
    print("Holes left: none")
else:
    print("Holes left: " + ", ".join(map(str, holes)))

