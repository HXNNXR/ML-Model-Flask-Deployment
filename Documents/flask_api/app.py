import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('model.pkl')

# Define the prediction function
def predict(data):
    return model.predict([data])

# Set up the Streamlit interface
st.title("Neurodevelopmental Disorder Prediction Tool")

# User inputs for the model (adjust based on your model's features)
age = st.number_input("Age", min_value=0, max_value=100, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])

# Button to trigger the prediction
if st.button("Get Prediction"):
    # Collect user input into a list (expand based on your model's input features)
    data = [age, 1 if gender == "Male" else 0]  # Example: converting gender to numerical (Male=1, Female=0)
    
    # Run prediction
    prediction = predict(data)
    
    # Display prediction result
    st.write(f"Prediction: {prediction[0]}")
