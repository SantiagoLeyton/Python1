# Ask the user to enter three numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Determine the greatest number
if number1 >= number2 and number1 >= number3:
    greatest = number1
elif number2 >= number1 and number2 >= number3:
    greatest = number2
else:
    greatest = number3

# Show the result
print("The greatest number is:", greatest)
