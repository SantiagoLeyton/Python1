# Show gym membership options
print("Gym membership options:")
print("1. 15 days - $18000")
print("2. 30 days - $35000")
print("3. 3 months - $86000")

# Ask the user to choose an option
option = int(input("Enter the option number (1, 2, or 3): "))

# Determine the cost
if option == 1:
    cost = 18000
    period = "15 days"
elif option == 2:
    cost = 35000
    period = "30 days"
elif option == 3:
    cost = 86000
    period = "3 months"
else:
    cost = 0
    period = "Invalid option"

# Show the result
if cost > 0:
    print("You chose the plan for", period, "and the cost is: $", cost)
else:
    print("Invalid option. Please restart the program and choose 1, 2, or 3.")