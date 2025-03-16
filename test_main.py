import pytest
from main import get_user_choice, get_computer_choice, determine_winner

def test_determine_winner():
    # Test ties
    assert determine_winner(1, 1) == "It's a tie!"
    assert determine_winner(2, 2) == "It's a tie!"
    assert determine_winner(3, 3) == "It's a tie!"
    assert determine_winner(4, 4) == "It's a tie!"
    assert determine_winner(5, 5) == "It's a tie!"
    
    # Test user wins
    assert determine_winner(1, 3) == "You win!"  # Rock beats Scissors
    assert determine_winner(1, 4) == "You win!"  # Rock beats Lizard
    assert determine_winner(2, 1) == "You win!"  # Paper beats Rock
    assert determine_winner(2, 5) == "You win!"  # Paper beats Spock
    assert determine_winner(3, 2) == "You win!"  # Scissors beats Paper
    assert determine_winner(3, 4) == "You win!"  # Scissors beats Lizard
    assert determine_winner(4, 2) == "You win!"  # Lizard beats Paper
    assert determine_winner(4, 5) == "You win!"  # Lizard beats Spock
    assert determine_winner(5, 1) == "You win!"  # Spock beats Rock
    assert determine_winner(5, 3) == "You win!"  # Spock beats Scissors
    
    # Test user loses
    assert determine_winner(1, 2) == "You lose!"  # Rock loses to Paper
    assert determine_winner(1, 5) == "You lose!"  # Rock loses to Spock
    assert determine_winner(2, 3) == "You lose!"  # Paper loses to Scissors
    assert determine_winner(2, 4) == "You lose!"  # Paper loses to Lizard
    assert determine_winner(3, 1) == "You lose!"  # Scissors loses to Rock
    assert determine_winner(3, 5) == "You lose!"  # Scissors loses to Spock
    assert determine_winner(4, 1) == "You lose!"  # Lizard loses to Rock
    assert determine_winner(4, 3) == "You lose!"  # Lizard loses to Scissors
    assert determine_winner(5, 2) == "You lose!"  # Spock loses to Paper
    assert determine_winner(5, 4) == "You lose!"  # Spock loses to Lizard

def test_get_computer_choice():
    choice = get_computer_choice()
    assert choice in [1, 2, 3, 4, 5]

# Note: Testing get_user_choice is tricky because it requires user input.
# You can mock input if needed, but it's generally not necessary for simple functions like this.

if __name__ == "__main__":
    pytest.main()