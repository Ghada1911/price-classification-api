from flask import Flask, request, jsonify
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import joblib

app = Flask(__name__)

# Load the trained model
best_model = joblib.load("best_price_classification_model.pkl")

# Load training data
train_data = pd.read_csv("train_dataset.csv")

# Drop 'id' and 'price_range' columns from training data
if 'id' in train_data.columns:
    train_data = train_data.drop("id", axis=1)

# Separate features and target variable
X_train = train_data.drop("price_range", axis=1)

# Fit SimpleImputer on training data
imputer = SimpleImputer(strategy='mean')
imputer.fit(X_train)

@app.route('/api/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.json

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Impute missing values
    df_imputed = imputer.transform(df)

    # Make predictions
    predictions = best_model.predict(df_imputed)

    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
