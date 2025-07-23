# This program calculates the total rental price for washing machines

# User input
print("What kind of washing machine do you want?")
print("1. big (4000 per hour)")
print("2. small (3000 per hour)")
kind = int(input("Enter the number: "))

# Price per hour
if kind == 1:
    price_per_hour = 4000
else:
    price_per_hour = 3000

# Total hours
hours = int(input("How many hours do you want to rent? "))
quantity = int(input("How many washing machines do you want? "))

# Calculate total
total = hours * price_per_hour * quantity

# Apply discount if needed
if quantity > 3:
    total = total * 0.97

# Output
print("Total price to pay: $" + str(round(total)))