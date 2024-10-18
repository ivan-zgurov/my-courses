tools = list(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances:
    tool = tools.pop(0)  # Queue behavior (FIFO)
    substance = substances.pop()  # Stack behavior (LIFO)
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print("Tools: " + ", ".join(map(str, tools)))
if substances:
    print("Substances: " + ", ".join(map(str, substances)))
if challenges:
    print("Challenges: " + ", ".join(map(str, challenges)))
