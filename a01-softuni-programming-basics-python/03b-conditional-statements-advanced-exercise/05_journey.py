total_budget = float(input())
season = input()
destination = ""
accommodation = ""
money_spend = 0


if total_budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        money_spend = total_budget * 0.3

    elif season == "winter":
        accommodation = "Hotel"
        money_spend = total_budget * 0.7


elif total_budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        money_spend = total_budget * 0.4

    elif season == "winter":
        accommodation = "Hotel"
        money_spend = total_budget * 0.8


else:
    destination = "Europe"
    accommodation = "Hotel"
    money_spend = total_budget * 0.9

print(f"Somewhere in {destination}")
print(f"{accommodation} - {money_spend:.2f}")
