import sys

# Greeting
print("Hello, I am a simple calculator who can handle basic arithmetic (+, -, *, /)")

# First user input: num1
num1 = input("Enter in your first number: ")

# Second user input: (+, -, *, /)
symbol = input("Pick +, -, *, /: ")

# Third user input: num2
num2 = input("Enter in your second number: ")

if (num1 or num2 > 0) and symbol == "/":
    print("Please use a number greater then zero")
    sys.exit()

# Figures out what symbol did the user pick: (+, -, *, /) and prints the equation and answer
if symbol == "+":
    print(f"{int (num1)} + {int (num2)} =", int(num1) + int(num2))

elif symbol == "-":
    print(f"{int (num1)} - {int (num2)} =", int(num1) - int(num2))

elif symbol == "*":
    print(f"{int (num1)} * {int (num2)} =", int(num1) * int(num2))

elif symbol == "/":
    print(f"{int (num1)} / {int (num2)} =", int(num1) / int(num2))
else:
    print("Invalid input or Please check your browser settings.")


