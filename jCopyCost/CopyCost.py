# Ask the user how many copies they want to print
copies = int(input("Enter the number of copies to print: "))

# Determine the price per copy based on the number of copies
if copies >= 0 and copies <= 499:
    price_per_copy = 120
elif copies >= 500 and copies <= 749:
    price_per_copy = 100
elif copies >= 750 and copies <= 999:
    price_per_copy = 80
else:
    price_per_copy = 50

# Calculate total cost
total_price = copies * price_per_copy

# Show the result
print("Price per copy: $" + str(price_per_copy))
print("Total price: $" + str(total_price))