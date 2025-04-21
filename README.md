# 🍷 Wine Quality Predictor & Visual Explorer

This project is a one-day data science portfolio piece where we analyze physicochemical properties of red wine and build a regression model to predict its quality. It also includes a simple interactive Streamlit app to demonstrate predictions.

---

## 🚀 Project Overview

Wine quality is influenced by multiple chemical attributes like acidity, sugar, and alcohol content. Using the UCI Red Wine Quality dataset, this project walks through:
- Data exploration and visualization (EDA)
- Correlation analysis
- Regression modeling (Linear and Random Forest)
- Interactive prediction tool using Streamlit

---

## 📁 Project Structure

wine-quality-proj/ 

  ├── data/ 
        │ └── winequality-red.csv # Raw dataset 
  
  ├── notebooks/ 
        │ └── EDA_and_Model.ipynb # Data exploration and model training 
  
  ├── app/ 
        │ └── app.py # Streamlit app for quality prediction 
  
  ├── requirements.txt # Python dependencies 
  
  └── README.md # Project documentation
---

## 📊 Dataset Details

- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- **Records**: ~1,599 red wine samples
- **Features**: 11 physicochemical inputs + 1 quality score (0–10)

Key features include:
- `fixed acidity`, `volatile acidity`, `citric acid`
- `residual sugar`, `chlorides`, `alcohol`
- Target variable: `quality`

---

## 🔍 Key Steps

### 1. Exploratory Data Analysis (EDA)
- Visualized distributions of wine quality
- Identified correlation of `alcohol`, `sulphates`, and `volatile acidity` with quality
- Cleaned and scaled features

### 2. Model Building
- Used **Linear Regression** as baseline
- Improved performance using **Random Forest Regressor**
- Evaluation metrics:
  - RMSE, MAE, R² Score

### 3. Streamlit App
- Allows user to input wine attributes via sliders
- Predicts wine quality using trained model
- Simple and lightweight app for demo purposes

---

## 🖥️ Running Locally

### 🔧 Setup
```bash
git clone https://github.com/yourusername/wine-quality-1day.git
cd wine-quality-1day
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd app
streamlit run app.py
