# Ask user if the computer beeps on startup
beep = input("Does the computer beep when it starts? (yes/no): ").lower()

# Ask user if the hard drive spins
drive_spins = input("Does the hard drive spin? (yes/no): ").lower()

# Determine the state of the computer based on the answers
if beep == "yes" and drive_spins == "yes":
    print("Contact technical support.")
elif beep == "yes" and drive_spins == "no":
    print("Check drive contacts.")
elif beep == "no" and drive_spins == "no":
    print("Bring the computer to the central repair center.")
elif beep == "no" and drive_spins == "yes":
    print("Check speaker connections.")
else:
    print("Invalid input. Please answer with 'yes' or 'no'.")
