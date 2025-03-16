from flask import Flask, request, jsonify
import random
import matplotlib.pyplot as plt
from stats import init_db, record_game, get_stats

app = Flask(__name__)

init_db()

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

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    
    if user_choice not in [1, 2, 3, 4, 5]:
        return jsonify({"error": "Invalid choice"}), 400
    
    computer_choice = get_computer_choice()
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    result = determine_winner(user_choice, computer_choice)
    
    record_game(user_choice, computer_choice, result)
    
    return jsonify({
        "user_choice": choices[user_choice - 1],
        "computer_choice": choices[computer_choice - 1],
        "result": result
    }), 200

@app.route('/stats', methods=['GET'])
def stats():
    stats = get_stats()
    user_wins = sum(1 for row in stats if row[2] == "You win!")
    computer_wins = sum(1 for row in stats if row[2] == "You lose!")
    ties = sum(1 for row in stats if row[2] == "It's a tie!")
    
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    user_choices = [row[0] for row in stats]
    computer_choices = [row[1] for row in stats]
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.bar(["User Wins", "Computer Wins", "Ties"], [user_wins, computer_wins, ties])
    plt.title("Game Results")
    
    plt.subplot(1, 2, 2)
    plt.hist([user_choices, computer_choices], bins=range(1, 7), label=["User", "Computer"], align='left')
    plt.xticks(range(1, 6), choices)
    plt.title("Choices Distribution")
    plt.legend()
    
    plt.savefig('stats.png')
    
    return jsonify({
        "user_wins": user_wins,
        "computer_wins": computer_wins,
        "ties": ties,
        "image": "stats.png"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)