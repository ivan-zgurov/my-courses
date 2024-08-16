price_per_killogram_veggies = float(input())
price_per_killogram_fruits = float(input())
amount_veggies_in_killograms = int(input())
amount_fruits_in_killograms = int(input())

total_income_in_leva = (
    price_per_killogram_veggies * amount_veggies_in_killograms
    + price_per_killogram_fruits * amount_fruits_in_killograms
)

total_income_in_euro = total_income_in_leva / 1.94

print(f"{total_income_in_euro:.2f}")
