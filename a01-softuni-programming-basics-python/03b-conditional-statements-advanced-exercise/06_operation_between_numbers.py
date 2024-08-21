number_a = int(input())
number_b = int(input())
operator = input()
sum = 0
even_or_odd = ""


if operator == "+":
    sum = number_a + number_b
    even_or_odd = "odd" if sum % 2 != 0 else "even"
    print(f"{number_a} {operator} {number_b} = {sum} - {even_or_odd}")
if operator == "-":
    sum = number_a - number_b
    even_or_odd = "odd" if sum % 2 != 0 else "even"
    print(f"{number_a} {operator} {number_b} = {sum} - {even_or_odd}")
if operator == "*":
    sum = number_a * number_b
    even_or_odd = "odd" if sum % 2 != 0 else "even"
    print(f"{number_a} {operator} {number_b} = {sum} - {even_or_odd}")
if operator == "/":
    if number_b == 0:
        print(f"Cannot divide {number_a} by zero")

    else:
        sum = number_a / number_b
        print(f"{number_a} / {number_b} = {sum:.2f}")

if operator == "%":
    if number_b == 0:
        print(f"Cannot divide {number_a} by zero")

    else:
        sum = number_a % number_b
        print(f"{number_a} % {number_b} = {sum}")
