import requests
import time
import math

url = "http://localhost:8080/set_state"
s = requests.Session()

t = 0
while True:
    time.sleep(0.04)
    t += 0.1
    angle = math.sin(t)
    delta_x = math.sin(0.3 * t) * 100
    state = {
        'angle': angle,
        'delta_x': delta_x,
        'timestamp': time.time(),
    }
    response = s.post(url, json=state)
    print(response.status_code, state)
