from flask import Flask, render_template
app = Flask(__name__)
@app.route("/fizzbuzz")
def home():
    numbers = []
    for num in range(1, 101):
        numbers.append(num)
    return render_template('index.html', numbers=numbers)