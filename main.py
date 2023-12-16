from flask import Flask
import random

correct_route=random.randint(1, 10)

app = Flask(__name__)

@app.route('/<int:num>')
def check_route(num):
    if num == correct_route:
        return '<h1>Higher</h1>'
    elif num > correct_route:
        return '<h1>Lower</h1>'
    else:
        return '<h1>Correct</h1>'


if __name__ == '__main__':
    app.run(debug=True)
