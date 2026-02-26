import os
import json
from flask import Flask, render_template, request, url_for, jsonify, session
from model import predict_crop_high_level
from ai_knowledge import AIFarmingAssistant
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure a folder to save uploaded plant images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'agriguard_ai_secret_key_2024'  # For session management
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Creates folder if it doesn't exist

# Initialize AI Assistant
ai_assistant = AIFarmingAssistant()

# Language translations for the interface
LANGUAGES = {
    "en": {"name": "English", "native": "English"},
    "hi": {"name": "Hindi", "native": "हिंदी"},
    "ta": {"name": "Tamil", "native": "தமிழ்"},
    "te": {"name": "Telugu", "native": "తెలుగు"},
    "bn": {"name": "Bengali", "native": "বাংলা"},
    "mr": {"name": "Marathi", "native": "मराठी"},
    "gu": {"name": "Gujarati", "native": "ગુજરાતી"},
    "kn": {"name": "Kannada", "native": "ಕನ್ನಡ"},
    "ml": {"name": "Malayalam", "native": "മലയാളം"}
}

@app.route('/')
def index():
    # Check if language is already selected
    if 'language' not in session:
        session['language'] = 'en'
    return render_template('index.html', languages=LANGUAGES, current_lang=session.get('language', 'en'))

@app.route('/set_language', methods=['POST'])
def set_language():
    """Set the preferred language for the user"""
    data = request.get_json()
    lang_code = data.get('language', 'en')
    if lang_code in LANGUAGES:
        session['language'] = lang_code
        ai_assistant.set_language(lang_code)
        return jsonify({"status": "success", "language": lang_code})
    return jsonify({"status": "error", "message": "Invalid language"}), 400

@app.route('/get_language')
def get_language():
    """Get current language setting"""
    return jsonify({
        "language": session.get('language', 'en'),
        "languages": LANGUAGES
    })

@app.route('/ai_chat', methods=['POST'])
def ai_chat():
    """AI Chat endpoint - provides detailed responses like ChatGPT"""
    data = request.get_json()
    query = data.get('message', '')
    crop_type = data.get('crop_type', None)
    language = session.get('language', 'en')
    
    # Set language for AI response
    ai_assistant.set_language(language)
    
    # Get comprehensive response from AI
    response = ai_assistant.get_response(query, crop_type)
    
    return jsonify({
        "status": "success",
        "response": response,
        "language": language
    })

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    """Analyze uploaded leaf image for disease detection"""
    file = request.files.get('image')
    if not file or file.filename == '':
        return jsonify({"status": "error", "message": "No image uploaded"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Run AI image analysis
    result = ai_assistant.analyze_image(filename)
    
    return jsonify({
        "status": "success",
        "analysis": result['analysis'],
        "recommendations": result['recommendations'],
        "timestamp": result['timestamp'],
        "image_url": url_for('static', filename='uploads/' + filename)
    })

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
