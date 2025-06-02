def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple Calculator")
print("Choose operation : +, -, *, /")

while True:
    op = input("Enter operation ( +, -, *, / or q to quit):")

    if op.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    if op not in ('+', '-', '*', '/'):
        print("Invalid operation! Please enter one of +, -, *, / or q to quit.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        
        print(f"The result of {num1} {op} {num2} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")