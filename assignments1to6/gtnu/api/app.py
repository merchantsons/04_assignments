from flask import Flask, render_template, request, jsonify, session
import random
import os
from werkzeug.middleware.proxy_fix import ProxyFix

# Initialize Flask app with correct static and template folder paths
app = Flask(__name__, 
           static_folder='../static',
           template_folder='../templates')

# Required for Vercel serverless environment
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

@app.route('/', methods=['GET'])
def index():
    try:
        # Initialize game state
        session['lower_bound'] = 1
        session['upper_bound'] = 100
        session['attempts'] = 0
        session['guess'] = random.randint(1, 100)  # Initial guess
        return render_template('index.html')
    except Exception as e:
        return str(e), 500

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        # Get feedback from user (too high, too low, or correct)
        user_feedback = request.form['feedback']
        current_guess = session.get('guess')
        lower_bound = session.get('lower_bound', 1)
        upper_bound = session.get('upper_bound', 100)
        attempts = session.get('attempts', 0)
        
        # Update attempts
        session['attempts'] = attempts + 1
        
        if user_feedback == 'correct':
            # Computer guessed correctly
            return jsonify({
                'result': 'success',
                'message': f"I got it in {session['attempts']} attempts! Your number is {current_guess}.",
                'game_over': True,
                'attempts': session['attempts']
            })
        
        elif user_feedback == 'too_high':
            # Computer guessed too high, adjust upper bound
            session['upper_bound'] = current_guess - 1
            upper_bound = current_guess - 1
            
        elif user_feedback == 'too_low':
            # Computer guessed too low, adjust lower bound
            session['lower_bound'] = current_guess + 1
            lower_bound = current_guess + 1
        
        # Check if bounds are valid
        if lower_bound > upper_bound:
            return jsonify({
                'result': 'error',
                'message': "I think there's been a mistake in your feedback. The range has no valid numbers.",
                'game_over': True,
                'attempts': session['attempts']
            })
        
        # Generate new guess based on updated bounds
        new_guess = random.randint(lower_bound, upper_bound)
        session['guess'] = new_guess
        
        return jsonify({
            'result': 'continue',
            'message': f"Is {new_guess} your number?",
            'guess': new_guess,
            'attempts': session['attempts'],
            'game_over': False
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset():
    try:
        # Reset game state
        session['lower_bound'] = 1
        session['upper_bound'] = 100
        session['attempts'] = 0
        session['guess'] = random.randint(1, 100)
        return jsonify({
            'message': 'Game reset successfully!',
            'initial_guess': session['guess']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Catch-all route to handle other paths
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

# For local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)