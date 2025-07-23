# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")
elif number == 0:
    print("Zero is not a valid number.")
else:
    print("The number is odd.")