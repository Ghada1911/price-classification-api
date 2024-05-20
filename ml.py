import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load datasets
train_data = pd.read_csv("train_dataset.csv")
test_data = pd.read_csv("test_dataset.csv")

# Drop 'id' and 'price_range' columns from training data, and 'id' from test data
if 'id' in train_data.columns:
    train_data = train_data.drop("id", axis=1)
if 'id' in test_data.columns:
    test_data = test_data.drop("id", axis=1)

# Separate features and target variable
X_train = train_data.drop("price_range", axis=1)
y_train = train_data["price_range"]

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(test_data)

# Split data into training and validation sets
X_train_split, X_val, y_train_split, y_val = train_test_split(X_train_imputed, y_train, test_size=0.2, random_state=42)

# Define and train multiple models
models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'GradientBoosting': GradientBoostingClassifier(random_state=42),
    'SVM': SVC(random_state=42)
}

# Evaluate each model
best_model = None
best_accuracy = 0

for name, model in models.items():
    model.fit(X_train_split, y_train_split)
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    print(f"{name} Accuracy: {accuracy}")
    
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

print("Best Model:", best_model)

# Save the best model
joblib.dump(best_model, "best_price_classification_model.pkl")

# Evaluate the best model
y_pred_best = best_model.predict(X_val)
conf_matrix_best = confusion_matrix(y_val, y_pred_best)
sns.heatmap(conf_matrix_best, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix of Best Model")
plt.show()

class_report_best = classification_report(y_val, y_pred_best)
print("Best Model Classification Report:\n", class_report_best)
