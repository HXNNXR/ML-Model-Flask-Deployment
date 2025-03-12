# ML-Model-Flask-Deployment
Deploying a Machine Learning Model with Flask 

I’ve built a simple Flask web app to deploy a machine learning model and make predictions accessible via an API endpoint. This allows others to interact with the model and receive real-time predictions through a POST request.

What’s Included:
Model Training: I trained a machine learning model to predict neurodevelopmental disorder severity in Sri Lankan children using a dataset related to public health and neurodevelopmental disorders.
Model Saving: I serialized the trained model into a .pkl file using joblib.
Flask API: A basic Flask app that loads the model and serves predictions via a simple API.
Deployment: The Flask app runs locally and can be accessed via http://127.0.0.1:5000.
