import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/failure_model.pkl")

# New sensor input
sample_data = pd.DataFrame(
    [[115, 9.5, 0.4, 1650, 125]],
    columns=[
        'temperature_c',
        'vibration_mm_s',
        'oil_pressure_bar',
        'rpm',
        'bearing_temp_c'
    ]
)

# Prediction
prediction = model.predict(sample_data)

print("Prediction:", prediction)

if prediction[0] == 1:
    print("⚠ Machine Failure Predicted")
else:
    print("✓ Machine Normal")