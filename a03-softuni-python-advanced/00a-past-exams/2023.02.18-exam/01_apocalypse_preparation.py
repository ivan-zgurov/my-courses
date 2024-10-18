textiles = list(map(int, input().split()))
medicaments = list(map(int, input().split()))

healing_items = {"Patch": 30, "Bandage": 40, "MedKit": 100}

created_items = {}

while textiles and medicaments:
    textile = textiles.pop(0)  # Queue behavior (FIFO)
    medicament = medicaments.pop()  # Stack behavior (LIFO)
    total = textile + medicament

    if total == healing_items["Patch"]:
        created_items["Patch"] = created_items.get("Patch", 0) + 1
    elif total == healing_items["Bandage"]:
        created_items["Bandage"] = created_items.get("Bandage", 0) + 1
    elif total >= healing_items["MedKit"]:
        created_items["MedKit"] = created_items.get("MedKit", 0) + 1
        remaining = total - healing_items["MedKit"]
        if remaining > 0 and medicaments:
            medicaments[-1] += remaining
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, amount in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    print(f"{item} - {amount}")

if medicaments:
    print("Medicaments left: " + ", ".join(map(str, reversed(medicaments))))
if textiles:
    print("Textiles left: " + ", ".join(map(str, textiles)))
