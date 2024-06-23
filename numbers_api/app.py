import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/odd')
def get_odd_number():
    odd_number = random.choice([num for num in range(1, 21) if num % 2 != 0])
    return jsonify({'odd_number': odd_number})

@app.route('/even')
def get_even_number():
    even_number = random.choice([num for num in range(1, 21) if num % 2 == 0])
    return jsonify({'even_number': even_number})

if __name__ == '__main__':
    app.run(debug=True)
