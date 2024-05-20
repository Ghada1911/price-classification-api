# Price Classification API



This repository contains a Flask-based API for predicting the price range of mobile devices using machine learning.

## Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Ghada1911/price-classification-api.git
   cd price-classification-api

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt

## Usage

1. **Run the API**:
   ```sh
   python main.py

2. **Make predictions**:

   Send a POST request to http://localhost:5000/api/predict with a JSON payload containing device specifications.
   Example JSON data:
   ```json
   
    {"battery_power": 1000, "blue": 1, "clock_speed": 1.5, "dual_sim": 0, "fc": 2, "four_g": 1, "int_memory": 16, "m_dep": 0.5, "mobile_wt": 200, "n_cores": 4, "pc": 8, "px_height": 800, "px_width": 1200, "ram": 4000, "sc_h": 10, "sc_w": 6, "talk_time": 10, "three_g": 1, "touch_screen": 1, "wifi": 1},
    {"battery_power": 1500, "blue": 0, "clock_speed": 2.0, "dual_sim": 1, "fc": 5, "four_g": 0, "int_memory": 32, "m_dep": 0.8, "mobile_wt": 150, "n_cores": 8, "pc": 12, "px_height": 1000, "px_width": 1600, "ram": 6000, "sc_h": 12, "sc_w": 8, "talk_time": 8, "three_g": 0, "touch_screen": 0, "wifi": 1}


3. **Response**:

   The API will respond with a JSON array containing predicted price ranges.


## Development

### Training and Evaluating Models 

- `ml.py`: Contains the code for training, evaluating, and saving the best machine learning model.
  
  To run:
  ```sh
  python ml.py

### Testing

- `test_api.py`: Contains integration tests for the API.
  
  To run:
  ```sh
  python test_api.py
