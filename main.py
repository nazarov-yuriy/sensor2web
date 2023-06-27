from flask import Flask, jsonify, render_template
import math

app = Flask(__name__)

t = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_state')
def get_angle():
    global t
    t += 0.1
    angle = math.sin(t)
    delta_x = math.sin(0.3 * t)
    return jsonify({
        'angle': angle,
        'delta_x': delta_x
    })


if __name__ == "__main__":
    app.run(debug=True, port=8080)
