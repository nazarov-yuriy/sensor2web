from flask import Flask, jsonify, render_template, request
import math

app = Flask(__name__)

allowed_keys = {'angle', 'delta_x'}
state = {
    'angle': 0,
    'delta_x': 0
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_state')
def get_state_():
    return jsonify(state)


@app.route('/set_state', methods=['POST'])
def get_state():
    global state
    data = request.get_json()
    if not set(data.keys()).issubset(allowed_keys):
        return "Wrong data", 400
    state = data
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
