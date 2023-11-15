a = input("Expression: ")
num1, op, num2 = a.split(" ")
num1 = float(num1)
num2 = float(num2)

if op == "+":
    ans = num1 + num2
elif op == "-":
    ans = num1 - num2
elif op == "*":
    ans = num1 * num2
elif op == "/":
    ans = round((num1 / num2), 1)

print(ans)