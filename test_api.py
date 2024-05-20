import requests
import json

# API endpoint URL
url = 'http://127.0.0.1:5000/api/predict'

# JSON data containing device specifications
data = [
    {"battery_power": 1000, "blue": 1, "clock_speed": 1.5, "dual_sim": 0, "fc": 2, "four_g": 1, "int_memory": 16, "m_dep": 0.5, "mobile_wt": 200, "n_cores": 4, "pc": 8, "px_height": 800, "px_width": 1200, "ram": 4000, "sc_h": 10, "sc_w": 6, "talk_time": 10, "three_g": 1, "touch_screen": 1, "wifi": 1},
    {"battery_power": 1500, "blue": 0, "clock_speed": 2.0, "dual_sim": 1, "fc": 5, "four_g": 0, "int_memory": 32, "m_dep": 0.8, "mobile_wt": 150, "n_cores": 8, "pc": 12, "px_height": 1000, "px_width": 1600, "ram": 6000, "sc_h": 12, "sc_w": 8, "talk_time": 8, "three_g": 0, "touch_screen": 0, "wifi": 1}
]

# Send POST requests
response = requests.post(url, json=data)

# Print response
print(response.json())
