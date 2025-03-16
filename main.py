import random

def get_user_choice():
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")
    choice = int(input("Enter the number of your choice: "))
    return choice

def get_computer_choice():
    return random.randint(1, 5)

def determine_winner(user_choice, computer_choice):
    winning_combinations = {
        1: [3, 4],  # Rock beats Scissors and Lizard
        2: [1, 5],  # Paper beats Rock and Spock
        3: [2, 4],  # Scissors beats Paper and Lizard
        4: [2, 5],  # Lizard beats Paper and Spock
        5: [1, 3]   # Spock beats Rock and Scissors
    }
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in winning_combinations[user_choice]:
        return "You win!"
    else:
        return "You lose!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    print(f"You chose: {choices[user_choice - 1]}")
    print(f"Computer chose: {choices[computer_choice - 1]}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()