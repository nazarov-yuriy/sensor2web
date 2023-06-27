from flask import Flask, jsonify, render_template
import math

app = Flask(__name__)

angle = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_angle')
def get_angle():
    global angle
    angle += 0.1
    return jsonify({'angle': math.sin(angle)})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
