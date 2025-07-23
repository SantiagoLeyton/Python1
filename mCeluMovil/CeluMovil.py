# Ask the user for their mobile operator
operator = input("Enter your mobile operator (Tigo, Claro, Movistar): ").lower()

# Ask how many international minutes were used
international_minutes = int(input("Enter the number of international minutes used: "))

# Set charges based on operator
if operator == "tigo":
    fixed_charge = 45000
    international_rate = 200
    data_package = 12000
elif operator == "claro":
    fixed_charge = 30000
    international_rate = 100
    data_package = 18000
elif operator == "movistar":
    fixed_charge = 40000
    international_rate = 250
    data_package = 8000
else:
    print("Invalid operator.")
    exit()

# Calculate total cost
international_cost = international_minutes * international_rate
total = fixed_charge + international_cost + data_package

# Show the result
print("\n--- Bill Summary ---")
print("Operator:", operator.capitalize())
print("Fixed charge:", fixed_charge)
print("International minutes:", international_minutes)
print("International cost:", international_cost)
print("Data package:", data_package)
print("Total to pay:", total)
