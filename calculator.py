def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division by zero"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print("Result:", addition(num1, num2))
elif operation == '2':
    print("Result:", subtraction(num1, num2))
elif operation == '3':
    print("Result:", multiplication(num1, num2))
elif operation == '4':
    print("Result:", division(num1, num2))
else:
    print("You entered an invalid operation number")