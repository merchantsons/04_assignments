from flask import Flask, render_template, request
import random
import string

# Initialize Flask app with correct static and template folder paths
app = Flask(__name__,
            static_folder='../static',  # Static files in 'static' folder one level up
            template_folder='../templates')  # Templates in 'templates' folder one level up


def generate_password(length=12, include_numbers=True, include_special=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        numbers = 'numbers' in request.form
        special = 'special' in request.form
        password = generate_password(length, numbers, special)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)