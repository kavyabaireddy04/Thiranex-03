import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load Dataset
data = pd.read_csv(r"C:\Users\kotireddy81\OneDrive\Desktop\AirPassengers.csv")
print(data.columns)

print("First 5 Records:")
print(data.head())

# Create numerical index for months
data["Month_Number"] = range(1, len(data) + 1)

# Features and Target
X = data[["Month_Number"]]
y = data["#Passengers"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict Existing Values
y_pred = model.predict(X)

# Predict Future 12 Months
future_months = pd.DataFrame({
    "Month_Number": range(len(data)+1, len(data)+13)
})

future_predictions = model.predict(future_months)

# Model Accuracy
mse = mean_squared_error(y, y_pred)

print("\nMean Squared Error:", mse)

print("\nFuture Passenger Predictions:")
for i, value in enumerate(future_predictions, start=1):
    print(f"Future Month {i}: {int(value)} passengers")

# Visualization
plt.figure(figsize=(10,6))

plt.scatter(X, y, label="Actual Data")

plt.plot(X, y_pred, label="Regression Line")

plt.plot(
    future_months,
    future_predictions,
    linestyle='dashed',
    label="Future Prediction"
)

plt.xlabel("Month Number")
plt.ylabel("Passengers")
plt.title("Predictive Analytics Using Historical Data")
plt.legend()
plt.grid(True)

plt.show()