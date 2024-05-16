from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Hello, this is a basic ML model deployment......!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array([[data['experience']]]))
    output = prediction[0]
    return jsonify({'salary': output})

if __name__ == '__main__':
    app.run(debug=True)
