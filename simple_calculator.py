# Greeting
print("Hello, I am a simple calculator who can handle basic arithmetic (+, -, *, /)")

# First user input: num1
num1 = input("Enter in your first number: ")

# if num1 == int(num1):
#     pass

# Second user input: (+, -, *, /)
symbol = input("Pick +, -, *, /: ")

# Third user input: num2
num2 = input("Enter in your second number: ")
# if num2 == int(num2):
#     pass



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


