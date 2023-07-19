import wandb

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
wandb.init(project="pendulum")

allowed_keys = {'angle', 'delta_x'}
state = {
    'angle': 0,
    'delta_x': 0
}
data = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_state')
def get_state_():
    return jsonify(state)


@socketio.on('connect')
def test_connect(auth):
    emit('system', {'data': 'Connected'})

@app.route('/set_state', methods=['POST'])
def set_state():
    global state
    data = request.get_json()
    if not set(data.keys()).issubset(allowed_keys):
        return "Wrong data", 400
    state = data
    socketio.emit('set_state', data)
    wandb.log(data)
    return "ok"


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=8080)
