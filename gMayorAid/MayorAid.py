# Ask for user gender and age
gender = input("Enter your gender (male/female): ").lower()
age = int(input("Enter your age: "))

# Calculate the support amount
if gender == "female":
    if age > 50:
        support = 120000
    elif age >= 30:
        support = 100000
    else:
        support = 0
elif gender == "male":
    support = 40000
else:
    support = 0

# Show the result
print("The monthly support you receive is: $", support)
