import requests
import time
import math

url = "http://localhost:8080/set_state"

t = 0
while True:
    time.sleep(0.1)
    t += 0.1
    angle = math.sin(t)
    delta_x = math.sin(0.3 * t)
    state = {
        'angle': angle,
        'delta_x': delta_x
    }
    response = requests.post(url, json=state)
    print(response.status_code, state)
