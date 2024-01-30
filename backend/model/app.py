import streamlit as st
import numpy as np
import pandas as pd
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
# Load data
df = pd.read_csv("/home/atharva/Desktop/jugadu-trio-2.0/backend/model/data.csv")
# Drop NaN values and convert 'diagnosis' to categorical
df = df.dropna(axis=1)
df['diagnosis'] = df['diagnosis'].astype('category')
# Data Splitting and Feature Scaling
X = df.iloc[:, 2:32].values
Y = df.iloc[:, 1].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Model Training
forest = RandomForestClassifier(random_state=0, criterion="entropy", n_estimators=10)
forest.fit(X_train, Y_train)
# Model Evaluation
Y_pred = forest.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
# Save the trained model
dump(forest, "Cancer_prediction.joblib")
# Streamlit App
st.title("Breast Cancer Prediction")
# Collect user input for each feature
radius_mean = st.text_input("Radius Mean", value="0")
texture_mean = st.text_input("Texture Mean", value="0")
perimeter_mean = st.text_input("Perimeter Mean", value="0")
area_mean = st.text_input("Area Mean", value="0")
smoothness_mean = st.text_input("Smoothness Mean", value="0")
compactness_mean = st.text_input("Compactness Mean", value="0")
concavity_mean = st.text_input("Concavity Mean", value="0")
concave_points_mean = st.text_input("Concave Points Mean", value="0")
symmetry_mean = st.text_input("Symmetry Mean", value="0")
fractal_dimension_mean = st.text_input("Fractal Dimension Mean", value="0")
radius_se = st.text_input("Radius SE", value="0")
texture_se = st.text_input("Texture SE", value="0")
perimeter_se = st.text_input("Perimeter SE", value="0")
area_se = st.text_input("Area SE", value="0")
smoothness_se = st.text_input("Smoothness SE", value="0")
compactness_se = st.text_input("Compactness SE", value="0")
concavity_se = st.text_input("Concavity SE", value="0")
concave_points_se = st.text_input("Concave Points SE", value="0")
symmetry_se = st.text_input("Symmetry SE", value="0")
fractal_dimension_se = st.text_input("Fractal Dimension SE", value="0")
radius_worst = st.text_input("Radius Worst", value="0")
texture_worst = st.text_input("Texture Worst", value="0")
perimeter_worst = st.text_input("Perimeter Worst", value="0")
area_worst = st.text_input("Area Worst", value="0")
smoothness_worst = st.text_input("Smoothness Worst", value="0")
compactness_worst = st.text_input("Compactness Worst", value="0")
concavity_worst = st.text_input("Concavity Worst", value="0")
concave_points_worst = st.text_input("Concave Points Worst", value="0")
symmetry_worst = st.text_input("Symmetry Worst", value="0")
fractal_dimension_worst = st.text_input("Fractal Dimension Worst", value="0")

user_data = np.array([[float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean),
                       float(smoothness_mean), float(compactness_mean), float(concavity_mean),
                       float(concave_points_mean), float(symmetry_mean), float(fractal_dimension_mean),
                       float(radius_se), float(texture_se), float(perimeter_se), float(area_se),
                       float(smoothness_se), float(compactness_se), float(concavity_se),
                       float(concave_points_se), float(symmetry_se), float(fractal_dimension_se),
                       float(radius_worst), float(texture_worst), float(perimeter_worst), float(area_worst),
                       float(smoothness_worst), float(compactness_worst), float(concavity_worst),
                       float(concave_points_worst), float(symmetry_worst), float(fractal_dimension_worst),
                       ]])
# Make a prediction using the pre-trained model
prediction = forest.predict(user_data)[0]
# Display the prediction result
# st.success(f"Prediction: {prediction}")
if st.button("Predict"):
    # # Prepare user input for prediction
    # user_data = np.array([[float(radius_mean), float(texture_mean), float(perimeter_mean),  # ... repeat for other features
    #                        float(fractal_dimension_worst)]])
    #
    # # Make a prediction using the pre-trained model
    # prediction = forest.predict(user_data)[0]
    #
    # # Display the prediction result
    st.success(f"Prediction: {prediction}")
    payload = {'prediction': prediction}
    response = requests.post('http://localhost:8000/model/api/save_prediction/', json=payload)
    if response.status_code == 200:
        st.success("Prediction result saved in the Django database.")
    else:
        st.error("Failed to save prediction result in the Django database. Please check the server logs.")