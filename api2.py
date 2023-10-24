from flask import Flask, json, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to HR Solution API'

# Create a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.get_json()

    # Ensure that the input data includes all required features
    required_features = ['JoiningYear', 'PaymentTier', 'Age', 'Experience(year)',
                         'Edu_rank', 'EverBenched_Yes', 'Gender_Male', 'Age_range_Youths']

    if not all(feature in data for feature in required_features):
        return jsonify({'error': 'Missing required features'}), 400

    # Prepare the input data for prediction
    input_data = []
    for feature in required_features:
        input_data.append(data[feature])

    # Make a prediction using the loaded model
    prediction = model.predict([input_data])

     # Convert the prediction result to a user-friendly response
    result = "will go on leave" if prediction == 1 else "will not go on leave"

    # Return the prediction as a response
    return jsonify({'This staff': result})

if __name__ == '__main__':
    app.run(debug=True)