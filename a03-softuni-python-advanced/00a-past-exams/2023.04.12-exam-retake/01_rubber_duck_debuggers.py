programmer_times = list(map(int, input().split()))
tasks = list(map(int, input().split()))

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while programmer_times and tasks:
    programmer_time = programmer_times.pop(0)  # Queue behavior (FIFO)
    task = tasks.pop()  # Stack behavior (LIFO)
    total_time = programmer_time * task

    if 0 <= total_time <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= total_time <= 120:
        ducks["Thor Ducky"] += 1
    elif 121 <= total_time <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= total_time <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        tasks.append(task - 2)
        programmer_times.append(programmer_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks['Darth Vader Ducky']}")
print(f"Thor Ducky: {ducks['Thor Ducky']}")
print(f"Big Blue Rubber Ducky: {ducks['Big Blue Rubber Ducky']}")
print(f"Small Yellow Rubber Ducky: {ducks['Small Yellow Rubber Ducky']}")
