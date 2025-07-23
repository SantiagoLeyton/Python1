# Ask user for the model number of the car
model_number = int(input("Enter your car's model number: "))

# List of defective model numbers
defective_models = [119, 179, 189, 190, 191, 192, 193, 194, 195, 221, 780]

# Check if the model number is defective
if model_number in defective_models:
    print("Your car is defective, please take it to warranty service.")
else:
    print("Your car is not defective.")
