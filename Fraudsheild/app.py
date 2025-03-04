from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Mock fraud detection model
model = IsolationForest(contamination=0.01)

@app.route('/detect', methods=['POST'])
def detect_fraud():
    data = request.json['transactions']
    predictions = model.fit_predict(np.array(data).reshape(-1, 1))
    return jsonify({"fraudulent_transactions": (predictions == -1).tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)