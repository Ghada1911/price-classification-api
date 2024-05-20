# Price Classification API

![Build Status](https://github.com/Ghada1911/price-classification-api/actions/workflows/main.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/Ghada1911/price-classification-api/badge.svg?branch=main)](https://coveralls.io/github/Ghada1911/price-classification-api?branch=main)

This repository contains a Flask-based API for predicting the price range of mobile devices using machine learning.

## Project Structure
price-classification-api/
│
├── data/
│ ├── train_dataset.csv
│ └── test_dataset.csv
│
├── models/
│ └── best_price_classification_model.pkl
│
├── main.py
├── ml.py
├── test_api.py
├── requirements.txt
└── README.md


## Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Ghada1911/price-classification-api.git
   cd price-classification-api

