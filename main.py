from flask import Flask
import random

correct_route=random.randint(1, 10)

app = Flask(__name__)

def create_buttons():
    buttons = ''
    for i in range(1, 11):
        buttons += f"<a href='/{i}' style='margin-right:10px; text-decoration=none'>{i}</a>"
    return buttons

def add_choices_decorator(func):
    def wrapper(num):
        return f"{create_buttons()}"\
                f"{func(num)}"
    return wrapper


@app.route('/<int:num>')
@add_choices_decorator
def check_route(num):
    if num < correct_route:
        return '<h1>Higher</h1>'\
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Animated GIF">'
    elif num > correct_route:
        return '<h1>Lower</h1>'\
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Animated GIF">'
    else:
        return '<h1>Correct</h1>'\
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Animated GIF">'

if __name__ == '__main__':
    app.run(debug=True)
