from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('fraud_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    features_array = np.array([features])
    prediction = model.predict(features_array)
    result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"
    return render_template('result.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
