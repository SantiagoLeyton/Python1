# We import the random module to generate random numbers (like drawing cards)
import random

# Generate two random cards for user and computer
user_cards = [random.randint(1, 10), random.randint(1, 10)]
computer_cards = [random.randint(1, 10), random.randint(1, 10)]

# Show user's cards
print("Your first two cards are:", user_cards)
user_total = sum(user_cards)

# Generate a hidden card for each
user_hidden = random.randint(1, 10)
computer_hidden = random.randint(1, 10)

# Ask user if they want to reveal their hidden card
choice = input("Press 'A' to reveal your hidden card: ").upper()

if choice == 'A':
    print("Your hidden card is:", user_hidden)
    user_total += user_hidden
else:
    print("You did not reveal the hidden card.")
    user_total += 0

# Reveal computer's total
computer_total = sum(computer_cards) + computer_hidden
print("\nComputer's cards were:", computer_cards, "and hidden card:", computer_hidden)

# Show both totals
print("\nYour total is:", user_total)
print("Computer's total is:", computer_total)

# Determine winner
if user_total > 21 and computer_total > 21:
    print("Both players busted. No winner.")
elif user_total <= 21 and (computer_total > 21 or user_total > computer_total):
    print("You win!")
elif computer_total <= 21 and (user_total > 21 or computer_total > user_total):
    print("Computer wins!")
elif user_total == computer_total and user_total <= 21:
    print("It's a tie!")
