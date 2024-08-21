type_of_screening = input()
number_of_rows = int(input())
number_of_colums = int(input())
total_income = 0

if type_of_screening == "Premiere":
    total_income = number_of_colums * number_of_rows * 12

elif type_of_screening == "Normal":
    total_income = number_of_colums * number_of_rows * 7.5

elif type_of_screening == "Discount":
    total_income = number_of_colums * number_of_rows * 5

print(f"{total_income:.2f} leva")
