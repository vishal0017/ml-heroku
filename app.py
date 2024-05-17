import os
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Hello, this is a basic ML model deployment!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    experience = data['experience']
    prediction = model.predict(np.array([[experience]]))
    output = prediction[0]
    return jsonify({'salary': output})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
