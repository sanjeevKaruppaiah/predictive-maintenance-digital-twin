import pandas as pd

data_path = "data/maintenance_sensor_data.csv"

df = pd.read_csv(data_path)

print("Columns in dataset:")
print(df.columns)

print("\nFirst few rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())
plt.figure(figsize=(10,5))
plt.plot(df['temperature_c'])
plt.title("Temperature Trend")
plt.show()
