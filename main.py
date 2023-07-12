print("Hello World!")
import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Invalid choice. Please try again.")

# Main game loop
print("Let's play Rock, Paper, Scissors!")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(result)

    if not play_again():
        break

print("Thanks for playing!")

