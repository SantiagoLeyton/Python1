# Ask the user to enter grades for five subjects
physics = float(input("Enter your Physics grade (0 to 10): "))
chemistry = float(input("Enter your Chemistry grade (0 to 10): "))
biology = float(input("Enter your Biology grade (0 to 10): "))
math = float(input("Enter your Math grade (0 to 10): "))
computing = float(input("Enter your Computing grade (0 to 10): "))

# Calculate the average
average = (physics + chemistry + biology + math + computing) / 5

# Show the average and the result message
print("Your average is:", average)

# Determine the final evaluation
if average < 6:
    print("Your performance is: Bad")
elif average <= 8:
    print("Your performance is: Good")
else:
    print("Your performance is: Excellent")
