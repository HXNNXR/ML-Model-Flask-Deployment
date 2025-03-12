import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model (update the path if needed)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Welcome to the model API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request (assumed to be in JSON format)
    data = request.get_json()

    # Extract the features (this depends on how your model works)
    # Make sure to replace 'feature1', 'feature2', etc. with your actual feature names
    feature1 = data['feature1']
    feature2 = data['feature2']
    
    # Prepare the features as a list or array for the model
    features = [[feature1, feature2]]  # Example for two features, adjust accordingly

    # Predict using the loaded model
    prediction = model.predict(features)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
