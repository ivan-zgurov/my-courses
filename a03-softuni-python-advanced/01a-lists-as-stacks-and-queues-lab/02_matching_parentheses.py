algebraic_expression = input()
stack = []

for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == "(":
        stack.append(index)
    elif algebraic_expression[index] == ")":
        most_recent_parentheses_index = stack.pop()
        print(algebraic_expression[most_recent_parentheses_index : index + 1])
