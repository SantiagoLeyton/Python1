# Ask for sandwich size
size = input("Enter sandwich size (small or large): ").lower()

# Set base price
if size == "small":
    price = 6000
elif size == "large":
    price = 12000
else:
    print("Invalid size selected.")
    exit()

# Ask for extra ingredients
print("Do you want the following ingredients? (yes or no)")

bacon = input("Bacon (+3000): ").lower()
jalapeno = input("Jalapeno (+0): ").lower()
turkey = input("Turkey (+3000): ").lower()
cheese = input("Cheese (+2500): ").lower()

# Add ingredient prices
if bacon == "yes":
    price += 3000
if jalapeno == "yes":
    price += 0
if turkey == "yes":
    price += 3000
if cheese == "yes":
    price += 2500

# Show final order summary
print("\n--- Sandwich Order Summary ---")
print("Size:", size)
print("Includes bacon:", bacon)
print("Includes jalapeno:", jalapeno)
print("Includes turkey:", turkey)
print("Includes cheese:", cheese)
print("Total to pay:", price)
