import random

def get_user_choice():
    user = input("Enter Rock, paper, or scissors: ")
    if user not in ['Rock', 'paper', 'scissors']:
        print("Invalid choice! Try again.")
        return get_user_choice()
    return user

def get_computer_choice():
    return random.choice(['Rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Main game
user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(f"\nYour choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")
print(decide_winner(user_choice, computer_choice))