import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load("models/failure_model.pkl")

st.title("Predictive Maintenance Dashboard")

temp = st.slider("Temperature", 50, 150, 80)
vibration = st.slider("Vibration", 0, 15, 3)
pressure = st.slider("Oil Pressure", 0, 10, 4)
rpm = st.slider("RPM", 500, 3000, 1500)
bearing = st.slider("Bearing Temp", 50, 150, 80)

data = pd.DataFrame([[temp,vibration,pressure,rpm,bearing]],
columns=[
'temperature_c',
'vibration_mm_s',
'oil_pressure_bar',
'rpm',
'bearing_temp_c'
])

if st.button("Predict Machine Health"):

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠ Machine Failure Risk")
    else:
        st.success("✓ Machine Normal")
