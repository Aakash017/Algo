def evalRPN(tokens):
    operators = {"+", "-", "*", "/"}
    stack = []
    for char in tokens:
        if char not in operators:
            stack.append(char)
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if char == "+":
                r = num2 + num1
            elif char == "-":
                r = num2 - num1
            elif char == "*":
                r = num2 * num1
            else:
                r = int(num2 / num1)
            stack.append(r)
    return stack[-1]


print(evalRPN(["2", "1", "+", "3", "*"]))
