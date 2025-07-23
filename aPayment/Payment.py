# Ask for the employee's name
name = input("Please enter your name: ")

# Ask for the number of hours worked
hours = int(input("Enter the number of hours worked this week: "))

# Calculate the salary based on the number of hours
if hours <= 10:
    salary = hours * 30000
else:
    salary = hours * 33000

# Display the final message
print("Mr.", name, ", the number of hours is", hours, "and your total salary is", salary)