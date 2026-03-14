import random
import time

def generate_sensor_data():

    data = {
        "temperature_c": random.uniform(70,120),
        "vibration_mm_s": random.uniform(2,10),
        "oil_pressure_bar": random.uniform(0.3,6),
        "rpm": random.uniform(1400,1800),
        "bearing_temp_c": random.uniform(70,130)
    }

    return data


if __name__ == "__main__":

    while True:
        sensor = generate_sensor_data()
        print(sensor)
        time.sleep(2)
