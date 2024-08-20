person_age = float(input())
person_gender = input()

if person_gender == "m":
    if person_age < 16:
        print("Master")
    else:
        print("Mr.")

elif person_gender == "f":
    if person_age < 16:
        print("Miss")
    else:
        print("Ms.")
