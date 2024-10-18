fuel = list(map(int, input().split()))
consumption = list(map(int, input().split()))
needed_fuel = list(map(int, input().split()))

reached_altitudes = []
altitude_num = 1

while fuel and consumption and needed_fuel:
    current_fuel = fuel.pop()  # Take last fuel quantity
    current_consumption = consumption.pop(0)  # Take first consumption index
    result = current_fuel - current_consumption

    if result >= needed_fuel[0]:
        print(f"John has reached: Altitude {altitude_num}")
        reached_altitudes.append(f"Altitude {altitude_num}")
        needed_fuel.pop(0)
        altitude_num += 1
    else:
        print(f"John did not reach: Altitude {altitude_num}")
        break

if len(reached_altitudes) == len(needed_fuel) + len(reached_altitudes):
    print("John has reached all the altitudes and managed to reach the top!")
elif reached_altitudes:
    print("John failed to reach the top.")
    print("Reached altitudes: " + ", ".join(reached_altitudes))
else:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
