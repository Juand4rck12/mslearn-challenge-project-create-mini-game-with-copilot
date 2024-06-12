import random

# Write "hello word" to the console
print("Hello World")
wins = 0
rounds = 0

while True:
    # Get user input
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check if user input is valid
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    # Generate computer's choice
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")

    rounds += 1

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Game over!")
print(f"Number of wins: {wins}")
print(f"Number of rounds played: {rounds}")