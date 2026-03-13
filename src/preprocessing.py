import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/maintenance_sensor_data.csv")
print(df['failure_imminent'].value_counts())
failure_rate = df['failure_imminent'].mean()
print("Failure Rate:", failure_rate)
X = df[['temperature_c','vibration_mm_s','oil_pressure_bar','rpm','bearing_temp_c']]
y = df['failure_imminent']