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
  
   test data used:
   ```json
   
    {"battery_power": 1043, "blue": 1, "clock_speed": 1.8, "dual_sim": 1, "fc": 14, "four_g": 0, "int_memory": 5, "m_dep": 0.1, "mobile_wt": 193, "n_cores": 3, "pc": 16, "px_height": 226, "px_width": 1412, "ram": 3476, "sc_h": 12, "sc_w": 7, "talk_time": 2, "three_g": 0, "touch_screen": 1, "wifi": 0},
    {"battery_power": 841, "blue": 1, "clock_speed": 0.5, "dual_sim": 1, "fc": 4, "four_g": 1, "int_memory": 61, "m_dep": 0.8, "mobile_wt": 191, "n_cores": 5, "pc": 12, "px_height": 746, "px_width": 857, "ram": 3895, "sc_h": 6, "sc_w": 0, "talk_time": 7, "three_g": 1, "touch_screen": 0, "wifi": 0},
    {"battery_power": 1807, "blue": 1, "clock_speed": 2.8, "dual_sim": 0, "fc": 1, "four_g": 0, "int_memory": 27, "m_dep": 0.9, "mobile_wt": 186, "n_cores": 3, "pc": 4, "px_height": 1270, "px_width": 1366, "ram": 2396, "sc_h": 17, "sc_w": 10, "talk_time": 10, "three_g": 0, "touch_screen": 1, "wifi": 1},
    {"battery_power": 1546, "blue": 0, "clock_speed": 0.5, "dual_sim": 1, "fc": 18, "four_g": 1, "int_memory": 25, "m_dep": 0.5, "mobile_wt": 96, "n_cores": 8, "pc": 20, "px_height": 295, "px_width": 1752, "ram": 3893, "sc_h": 10, "sc_w": 0, "talk_time": 7, "three_g": 1, "touch_screen": 1, "wifi": 0},
    {"battery_power": 1434, "blue": 0, "clock_speed": 1.4, "dual_sim": 0, "fc": 11, "four_g": 1, "int_memory": 49, "m_dep": 0.5, "mobile_wt": 108, "n_cores": 6, "pc": 18, "px_height": 749, "px_width": 810, "ram": 1773, "sc_h": 15, "sc_w": 8, "talk_time": 7, "three_g": 1, "touch_screen": 0, "wifi": 1},
    {"battery_power": 1464, "blue": 1, "clock_speed": 2.9, "dual_sim": 1, "fc": 5, "four_g": 1, "int_memory": 50, "m_dep": 0.8, "mobile_wt": 198, "n_cores": 8, "pc": 9, "px_height": 569, "px_width": 939, "ram": 3506, "sc_h": 10, "sc_w": 7, "talk_time": 3, "three_g": 1, "touch_screen": 1, "wifi": 1},
    {"battery_power": 1718, "blue": 0, "clock_speed": 2.4, "dual_sim": 0, "fc": 1, "four_g": 0, "int_memory": 47, "m_dep": 1.0, "mobile_wt": 156, "n_cores": 2, "pc": 3, "px_height": 1283, "px_width": 1374, "ram": 3873, "sc_h": 14, "sc_w": 2, "talk_time": 10, "three_g": 0, "touch_screen": 0, "wifi": 0},
    {"battery_power": 833, "blue": 0, "clock_speed": 2.4, "dual_sim": 1, "fc": 0, "four_g": 0, "int_memory": 62, "m_dep": 0.8, "mobile_wt": 111, "n_cores": 1, "pc": 2, "px_height": 1312, "px_width": 1880, "ram": 1495, "sc_h": 7, "sc_w": 2, "talk_time": 18, "three_g": 0, "touch_screen": 1, "wifi": 1},
    {"battery_power": 1111, "blue": 1, "clock_speed": 2.9, "dual_sim": 1, "fc": 9, "four_g": 1, "int_memory": 25, "m_dep": 0.6, "mobile_wt": 101, "n_cores": 5, "pc": 19, "px_height": 556, "px_width": 876, "ram": 3485, "sc_h": 11, "sc_w": 9, "talk_time": 10, "three_g": 1, "touch_screen": 1, "wifi": 0}


4. **Response**:
   
   The API will respond with a JSON array containing predicted price ranges.
   ```json
   [3, 3, 2, 3, 1, 3, 3, 1, 3] 

## Development

### Training and Evaluating Models 

- `ml.py`: Contains the code for training, evaluating, and saving the best machine learning model.
  
  To run:
  ```sh
  python ml.py

#### Model Performance

##### Best Model: SVC (SVC(random_state=42))

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.99      | 0.98   | 0.99     | 105     |
| 1     | 0.95      | 0.99   | 0.97     | 91      |
| 2     | 0.94      | 0.95   | 0.94     | 92      |
| 3     | 0.98      | 0.95   | 0.96     | 112     |


- **Accuracy:** 0.965
- **Macro Avg:**
  - Precision: 0.96
  - Recall: 0.97
  - F1-Score: 0.96
- **Weighted Avg:**
  - Precision: 0.97
  - Recall: 0.96
  - F1-Score: 0.97

##### Confusion matrix of the best model:

![Confusion Matrix](confusion_matrix.png)

### Testing

- `test_api.py`: Contains integration tests for the API.
  
  To run:
  ```sh
  python test_api.py
