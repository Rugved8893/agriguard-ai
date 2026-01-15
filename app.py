from flask import Flask, render_template, request
from model import predict_crop_loss

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    rainfall = float(request.form['rainfall'])
    temperature = float(request.form['temperature'])

    risk, loss = predict_crop_loss(rainfall, temperature)

    return render_template(
        'result.html',
        risk=risk,
        loss=loss
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
