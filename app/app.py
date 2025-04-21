import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load models
rf = joblib.load('C:/Users/bhava/OneDrive/Desktop/wine_quality_proj/models/rf_model.pkl')
xgb = joblib.load('C:/Users/bhava/OneDrive/Desktop/wine_quality_proj/models/xgb_model.pkl')
cat = joblib.load('C:/Users/bhava/OneDrive/Desktop/wine_quality_proj/models/cat_model.pkl')
ridge = joblib.load('C:/Users/bhava/OneDrive/Desktop/wine_quality_proj/models/ridge_model.pkl')

st.title("🍷 Wine Quality Predictor")

st.markdown("Adjust the sliders to simulate wine chemistry and predict its quality.")

# Define feature sliders
features = {
    'fixed acidity': st.slider('Fixed Acidity', 4.0, 16.0, 8.0),
    'volatile acidity': st.slider('Volatile Acidity', 0.1, 1.5, 0.5),
    'citric acid': st.slider('Citric Acid', 0.0, 1.0, 0.3),
    'residual sugar': st.slider('Residual Sugar', 0.5, 15.0, 2.5),
    'chlorides': st.slider('Chlorides', 0.01, 0.2, 0.05),
    'free sulfur dioxide': st.slider('Free Sulfur Dioxide', 1, 70, 15),
    'total sulfur dioxide': st.slider('Total Sulfur Dioxide', 6, 300, 50),
    'density': st.slider('Density', 0.9900, 1.0050, 0.9968),
    'pH': st.slider('pH', 2.8, 4.0, 3.3),
    'sulphates': st.slider('Sulphates', 0.2, 2.0, 0.6),
    'alcohol': st.slider('Alcohol', 8.0, 15.0, 10.0)
}

# Convert input into DataFrame
input_df = pd.DataFrame([features])

# Predict with each model
rf_pred = rf.predict(input_df)[0]
xgb_pred = xgb.predict(input_df)[0]
cat_pred = cat.predict(input_df)[0]
ridge_pred = ridge.predict(input_df)[0]

# Simple blend (equal weights)
blended_pred = (rf_pred + xgb_pred + cat_pred + ridge_pred) / 4

# Output
st.subheader(" Predicted Wine Quality:")
st.metric(label="Quality Score", value=f"{blended_pred:.2f}")