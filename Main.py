import random

def play_game():
    # Define game choices and their rules (Key beats Value)
    rules = {
        "stone": "scissors",
        "paper": "stone",
        "scissors": "paper"
    }
    
    # Track scores
    player_score = 0
    computer_score = 0
    
    print("========================================")
    print(" WELCOME TO SCISSORS, PAPER, STONE! ")
    print("========================================")
    print("Type 'quit' at any time to exit the game.\n")

    while True:
        # Get and clean user input
        user_choice = input("Enter your choice (Scissors, Paper, Stone): ").strip().lower()
        
        if user_choice == 'quit':
            print("\nThanks for playing!")
            print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
            break
            
        if user_choice not in rules:
            print("Invalid choice! Please type Scissors, Paper, or Stone.\n")
            continue
            
        # Generate random computer choice
        computer_choice = random.choice(list(rules.keys()))
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif rules[user_choice] == computer_choice:
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Display live score
        print(f"Scoreboard -> You: {player_score} | Computer: {computer_score}")
        print("----------------------------------------\n")

if __name__ == "__main__":
    play_game()
