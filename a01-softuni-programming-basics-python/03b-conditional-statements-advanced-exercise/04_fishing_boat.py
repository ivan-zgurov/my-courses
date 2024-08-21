available_budget = int(input())
season = input()
number_of_fishermen = int(input())
boat_rent_price = 0

if season == "Spring":
    boat_rent_price = 3000
elif season in ["Summer", "Autumn"]:
    boat_rent_price = 4200
elif season == "Winter":
    boat_rent_price = 2600

if number_of_fishermen <= 6:
    boat_rent_price *= 0.9
elif number_of_fishermen <= 11:
    boat_rent_price *= 0.85
else:
    boat_rent_price *= 0.75

if season != "Autumn" and number_of_fishermen % 2 == 0:
    boat_rent_price *= 0.95
difference = abs(boat_rent_price - available_budget)
if available_budget >= boat_rent_price:
    print(f"Yes! You have {difference:.2f} leva left.")
if available_budget < boat_rent_price:
    print(f"Not enough money! You need {difference:.2f} leva.")
