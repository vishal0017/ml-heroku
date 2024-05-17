import os
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
try:
    model = pickle.load(open('model.pkl', 'rb'))
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            raise Exception("Model is not loaded")
        
        data = request.get_json(force=True)
        print(f"Received data: {data}")
        
        experience = data['experience']
        print(f"Experience: {experience}")
        
        # Convert experience to a numeric value
        experience = float(experience)
        print(f"Numeric Experience: {experience}")
        
        prediction = model.predict(np.array([[experience]]))
        print(f"Prediction: {prediction}")
        
        output = prediction[0]
        return jsonify({'salary': output})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
