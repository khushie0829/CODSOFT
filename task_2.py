import random

# Function to get the computer's choice
def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Choose 'rock', 'paper', or 'scissors'.")
        
        # Get the user's choice
        user_choice = input("Enter your choice: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get the computer's choice
        comp_choice = computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, comp_choice)

        # Display the choices and result
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {comp_choice}")
        print(result)

        # Update score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScores: You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
