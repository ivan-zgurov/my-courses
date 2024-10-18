# 36 / 100

contestants = list(map(int, input().split()))
pies = list(map(int, input().split()))

while contestants and pies:
    current_contestant = contestants.pop(0)  # Take first contestant
    current_pie = pies.pop()  # Take last pie

    if current_contestant >= current_pie:
        current_contestant -= current_pie
        if current_contestant > 0:
            contestants.append(current_contestant)
    else:
        current_pie -= current_contestant
        if current_pie == 1 and pies:
            pies[-1] += 1
        elif current_pie == 1:
            pies.append(current_pie)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    if contestants:
        print("Contestants left: " + ", ".join(map(str, contestants)))
elif not pies and not contestants:
    print("We have a champion!")
elif pies and not contestants:
    print("Our contestants need to rest!")
    if pies:
        print("Pies left: " + ", ".join(map(str, pies)))

