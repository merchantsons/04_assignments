from flask import Flask, render_template, request, jsonify, send_from_directory
import random
import os

# Initialize Flask app with correct static and template folder paths
app = Flask(__name__, 
            static_folder='../static',
            template_folder='../templates')

class RockPaperScissors:
    def __init__(self, max_rounds=25):
        self.reset_game(max_rounds)

    def reset_game(self, max_rounds=25):
        """Reset the game state"""
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.max_rounds = max_rounds
        self.current_round = 0

    def play_round(self, player_choice):
        """Play a single round of Rock Paper Scissors"""
        # Validate input
        valid_choices = ['rock', 'paper', 'scissors']
        if player_choice not in valid_choices:
            raise ValueError("Invalid choice")

        # Computer makes a random choice
        computer_choice = random.choice(valid_choices)
        
        # Increment round
        self.current_round += 1

        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)

        # Update scores
        if result == 'player':
            self.player_score += 1
        elif result == 'computer':
            self.computer_score += 1
        else:
            self.ties += 1

        # Check if game is over
        game_over = (self.current_round >= self.max_rounds)

        return {
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'winner': result,
            'score': {
                'player': self.player_score,
                'computer': self.computer_score,
                'ties': self.ties
            },
            'current_round': self.current_round,
            'game_over': game_over
        }

    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of a round"""
        if player_choice == computer_choice:
            return 'tie'
        
        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combinations[player_choice] == computer_choice:
            return 'player'
        return 'computer'

# Create a global game instance
game = RockPaperScissors()

@app.route('/')
def index():
    """Render the main game page"""
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_game():
    """Handle game play requests"""
    try:
        # Get player's choice from request
        data = request.get_json()
        player_choice = data.get('choice', '').lower()

        # Play the round
        result = game.play_round(player_choice)

        # Return game result
        return jsonify({
            'success': True,
            'result': result
        })

    except ValueError as e:
        # Handle invalid input
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except Exception as e:
        # Handle any unexpected errors
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500

@app.route('/reset', methods=['POST'])
def reset_game():
    """Reset the game state"""
    try:
        game.reset_game()
        return jsonify({
            'success': True,
            'message': 'Game reset successfully'
        })
    except Exception as e:
        app.logger.error(f"Reset error: {e}")
        return jsonify({
            'success': False,
            'error': 'Could not reset the game'
        }), 500

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Logging Configuration
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    """Configure logging for the application"""
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler(
        'logs/rock_paper_scissors.log', 
        maxBytes=10240, 
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Rock Paper Scissors Application Startup')

# Application Configuration
def create_app():
    """Application factory"""
    setup_logging(app)
    return app

# Run the application
if __name__ == '__main__':
    application = create_app()
    app.run(
        host='0.0.0.0',  # Listen on all available network interfaces
        port=5000,       # Standard Flask development port
        debug=True       # Enable debug mode (set to False in production)
    )