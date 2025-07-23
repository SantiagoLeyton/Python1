# Ask the user to enter three angles
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

# Calculate the sum of the angles
total = angle1 + angle2 + angle3

# Check if the triangle is valid
if total == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
