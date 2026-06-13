# Predictive Analytics Using Historical Data

## Overview
This project focuses on predictive analytics using historical airline passenger data. A Linear Regression model is trained on past passenger records to identify trends and forecast future passenger counts.

The project demonstrates the complete predictive analytics workflow, including data preprocessing, model training, prediction, evaluation, and visualization.

---

## Objective
To build a predictive model that analyzes historical data and forecasts future trends using Machine Learning techniques.

---

## Dataset
Dataset Used: AirPassengers Dataset

Features:
- Month
- Number of Passengers

The dataset contains monthly airline passenger statistics collected over several years.

---

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## Methodology

### 1. Data Collection
The AirPassengers dataset was loaded from a CSV file.

### 2. Data Preprocessing
- Checked the dataset structure
- Converted month values into numerical indices
- Prepared input and output variables for model training

### 3. Model Development
A Linear Regression model was used to learn patterns from historical passenger data.

### 4. Prediction
The trained model was used to forecast passenger counts for the next 12 months.

### 5. Evaluation
Model performance was evaluated using Mean Squared Error (MSE).

### 6. Visualization
Graphs were generated to compare:
- Actual historical data
- Regression trend line
- Future predictions

---

## Results

Mean Squared Error (MSE):
2091.80

Future Passenger Forecasts:
- Month 1: 472
- Month 2: 475
- Month 3: 478
- Month 4: 480
- Month 5: 483
- Month 6: 486
- Month 7: 488
- Month 8: 491
- Month 9: 494
- Month 10: 496
- Month 11: 499
- Month 12: 502

The model successfully identified the increasing trend in passenger counts and generated future forecasts.

---

## Key Features
- Historical Data Analysis
- Data Preprocessing
- Linear Regression Model
- Future Trend Forecasting
- Performance Evaluation
- Data Visualization

---

## Project Structure

Predictive_Analytics_Project/
│
├── AirPassengers.csv
├── thiranex.py
├── prediction_graph.png
├── README.md
└── requirements.txt

---

## Output

The project generates:
- Future passenger predictions
- Mean Squared Error value
- Trend visualization graph

---

## Conclusion

This project successfully demonstrates predictive analytics using historical data. By applying Linear Regression, future passenger trends were forecasted based on historical records. The project provides practical experience in data preprocessing, machine learning, forecasting, and visualization techniques.
