import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load dataset
df = pd.read_csv("data/maintenance_sensor_data.csv")

# Features
X = df[['temperature_c',
        'vibration_mm_s',
        'oil_pressure_bar',
        'rpm',
        'bearing_temp_c']]

# Target
y = df['failure_imminent']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

# Train model
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

print("Model training completed")

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Save model
joblib.dump(model, "models/failure_model.pkl")

print("Model saved successfully")



importance = pd.Series(model.feature_importances_, index=X.columns)
print(importance)
import matplotlib.pyplot as plt

importance.sort_values().plot(kind='barh')
plt.title("Sensor Importance for Failure Prediction")
plt.show()