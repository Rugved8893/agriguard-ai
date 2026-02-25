import os
from flask import Flask, render_template, request, url_for
from model import predict_crop_high_level
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure a folder to save uploaded plant images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Creates folder if it doesn't exist

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/government')
def government():
    return render_template('government.html')

@app.route('/ngo')
def ngo():
    return render_template('ngo.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/suppliers')
def suppliers():
    return render_template('suppliers.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get user input (Dropdown and Numeric)
    crop_type = request.form.get('crop_type')
    rainfall = float(request.form.get('rainfall', 0))
    temperature = float(request.form.get('temperature', 0))
    humidity = float(request.form.get('humidity', 0))
    soil_ph = float(request.form.get('soil_ph', 0))
    
    # 2. Handle Image Upload (Advanced Feature)
    file = request.files.get('leaf_image')
    image_url = None
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Create a URL for the image to display it on the results page
        image_url = url_for('static', filename='uploads/' + filename)
    
    # 3. Call the prediction model
    result = predict_crop_high_level(rainfall, temperature, humidity, soil_ph, crop_type)
    
    return render_template('result.html', 
                           risk=result['risk_level'],
                           loss=result['estimated_loss'],
                           disease_alert=result['disease_alert'],
                           action_plan=result['action_plan'],
                           notes=result.get('analysis_notes', ''),
                           crop_type=crop_type,
                           user_image=image_url)

if __name__ == '__main__':
    app.run(debug=True)