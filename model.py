def predict_crop_high_level(rainfall, temperature, humidity, soil_ph, crop_type):
    # Comprehensive crop database with optimal parameters for Indian crops
    crop_thresholds = {
        # Cereals
        "Rice": {"min_rain": 150, "max_temp": 35, "ideal_ph": 6.0, "min_humidity": 70, "category": "Cereal"},
        "Wheat": {"min_rain": 50, "max_temp": 25, "ideal_ph": 6.5, "min_humidity": 40, "category": "Cereal"},
        "Maize": {"min_rain": 60, "max_temp": 32, "ideal_ph": 6.2, "min_humidity": 50, "category": "Cereal"},
        "Bajra": {"min_rain": 40, "max_temp": 35, "ideal_ph": 7.5, "min_humidity": 30, "category": "Cereal"},
        "Jowar": {"min_rain": 45, "max_temp": 35, "ideal_ph": 7.0, "min_humidity": 35, "category": "Cereal"},
        "Ragi": {"min_rain": 50, "max_temp": 32, "ideal_ph": 6.5, "min_humidity": 50, "category": "Cereal"},
        
        # Pulses
        "Gram": {"min_rain": 40, "max_temp": 30, "ideal_ph": 7.0, "min_humidity": 35, "category": "Pulse"},
        "Tur": {"min_rain": 60, "max_temp": 32, "ideal_ph": 6.5, "min_humidity": 50, "category": "Pulse"},
        "Moong": {"min_rain": 50, "max_temp": 35, "ideal_ph": 7.0, "min_humidity": 40, "category": "Pulse"},
        "Urad": {"min_rain": 50, "max_temp": 35, "ideal_ph": 7.0, "min_humidity": 40, "category": "Pulse"},
        "Masoor": {"min_rain": 35, "max_temp": 25, "ideal_ph": 6.8, "min_humidity": 35, "category": "Pulse"},
        
        # Cash Crops
        "Sugarcane": {"min_rain": 200, "max_temp": 40, "ideal_ph": 7.0, "min_humidity": 70, "category": "Cash Crop"},
        "Cotton": {"min_rain": 60, "max_temp": 40, "ideal_ph": 6.5, "min_humidity": 50, "category": "Cash Crop"},
        "Groundnut": {"min_rain": 50, "max_temp": 35, "ideal_ph": 6.2, "min_humidity": 40, "category": "Oilseed"},
        "Mustard": {"min_rain": 40, "max_temp": 25, "ideal_ph": 7.0, "min_humidity": 35, "category": "Oilseed"},
        "Soybean": {"min_rain": 60, "max_temp": 32, "ideal_ph": 6.5, "min_humidity": 50, "category": "Oilseed"},
        "Sunflower": {"min_rain": 50, "max_temp": 30, "ideal_ph": 6.5, "min_humidity": 45, "category": "Oilseed"},
        
        # Vegetables
        "Tomato": {"min_rain": 60, "max_temp": 30, "ideal_ph": 6.5, "min_humidity": 60, "category": "Vegetable"},
        "Potato": {"min_rain": 50, "max_temp": 25, "ideal_ph": 5.8, "min_humidity": 60, "category": "Vegetable"},
        "Onion": {"min_rain": 50, "max_temp": 32, "ideal_ph": 6.5, "min_humidity": 50, "category": "Vegetable"},
        "Cabbage": {"min_rain": 50, "max_temp": 25, "ideal_ph": 6.5, "min_humidity": 70, "category": "Vegetable"},
        "Cauliflower": {"min_rain": 50, "max_temp": 25, "ideal_ph": 6.5, "min_humidity": 70, "category": "Vegetable"},
        "Carrot": {"min_rain": 40, "max_temp": 28, "ideal_ph": 6.5, "min_humidity": 60, "category": "Vegetable"},
        "Brinjal": {"min_rain": 60, "max_temp": 35, "ideal_ph": 6.5, "min_humidity": 60, "category": "Vegetable"},
        "Okra": {"min_rain": 60, "max_temp": 35, "ideal_ph": 6.5, "min_humidity": 60, "category": "Vegetable"},
        "Green Chili": {"min_rain": 60, "max_temp": 32, "ideal_ph": 6.5, "min_humidity": 60, "category": "Vegetable"},
        "Ginger": {"min_rain": 150, "max_temp": 32, "ideal_ph": 6.0, "min_humidity": 80, "category": "Vegetable"},
        "Turmeric": {"min_rain": 150, "max_temp": 32, "ideal_ph": 6.0, "min_humidity": 80, "category": "Spice"},
        
        # Fruits
        "Mango": {"min_rain": 100, "max_temp": 40, "ideal_ph": 6.5, "min_humidity": 50, "category": "Fruit"},
        "Banana": {"min_rain": 150, "max_temp": 35, "ideal_ph": 6.5, "min_humidity": 70, "category": "Fruit"},
        "Papaya": {"min_rain": 100, "max_temp": 35, "ideal_ph": 6.5, "min_humidity": 60, "category": "Fruit"},
        "Guava": {"min_rain": 100, "max_temp": 35, "ideal_ph": 7.0, "min_humidity": 50, "category": "Fruit"},
        "Pomegranate": {"min_rain": 50, "max_temp": 40, "ideal_ph": 7.0, "min_humidity": 40, "category": "Fruit"},
        "Citrus": {"min_rain": 100, "max_temp": 35, "ideal_ph": 6.5, "min_humidity": 60, "category": "Fruit"},
        "Grapes": {"min_rain": 50, "max_temp": 35, "ideal_ph": 6.5, "min_humidity": 50, "category": "Fruit"},
        
        # Commercial Crops
        "Coffee": {"min_rain": 150, "max_temp": 28, "ideal_ph": 5.5, "min_humidity": 80, "category": "Commercial"},
        "Tea": {"min_rain": 150, "max_temp": 28, "ideal_ph": 5.0, "min_humidity": 80, "category": "Commercial"},
        "Rubber": {"min_rain": 200, "max_temp": 32, "ideal_ph": 5.5, "min_humidity": 80, "category": "Commercial"},
        "Tobacco": {"min_rain": 50, "max_temp": 35, "ideal_ph": 6.0, "min_humidity": 50, "category": "Commercial"},
        
        # Fodder
        "Berseem": {"min_rain": 80, "max_temp": 28, "ideal_ph": 7.0, "min_humidity": 60, "category": "Fodder"},
        "Lucerne": {"min_rain": 80, "max_temp": 30, "ideal_ph": 7.0, "min_humidity": 50, "category": "Fodder"},
    }

    # Default to Rice if crop not found
    limits = crop_thresholds.get(crop_type, crop_thresholds["Rice"])
    
    risk_score = 0
    reasons = []
    recommendations = []

    # 1. Dynamic Rainfall Analysis
    if rainfall < limits["min_rain"]:
        risk_score += 30
        reasons.append(f"Low rainfall ({rainfall}mm) - {crop_type} needs minimum {limits['min_rain']}mm")
        recommendations.append(f"Arrange supplemental irrigation - crop needs more water")
    
    # 2. Dynamic Temperature Analysis
    if temperature > limits["max_temp"]:
        risk_score += 25
        reasons.append(f"High temperature ({temperature}C) - optimal is below {limits['max_temp']}C")
        recommendations.append("Provide shade or mulching to reduce heat stress")
    elif temperature < limits["max_temp"] - 10:
        risk_score += 10
        reasons.append(f"Temperature is lower than ideal - may slow growth")

    # 3. Soil pH Health Check
    ph_diff = abs(soil_ph - limits["ideal_ph"])
    if ph_diff > 2.0:
        risk_score += 25
        reasons.append(f"Soil pH ({soil_ph}) is far from ideal ({limits['ideal_ph']})")
        recommendations.append("Apply lime for acidic soil or gypsum for alkaline soil")
    elif ph_diff > 1.0:
        risk_score += 10
        reasons.append(f"Soil pH slightly off ideal - minor adjustment needed")

    # 4. Humidity Analysis
    if humidity < limits["min_humidity"]:
        risk_score += 15
        reasons.append(f"Low humidity ({humidity}%) - {crop_type} prefers {limits['min_humidity']}%+")
        recommendations.append("Use drip irrigation to maintain moisture")

    # 5. Humidity-Pathogen Logic (Disease Risk)
    disease_warning = "Low Risk"
    if humidity > 85 and temperature > 20:
        risk_score += 20
        disease_warning = "High Risk - Fungal diseases likely"
        recommendations.append("Apply preventive fungicide - conditions favorable for fungal growth")
    elif humidity > 70 and temperature > 25:
        risk_score += 10
        disease_warning = "Moderate Risk - Monitor for pests"
        recommendations.append("Regular monitoring for pest infestation")

    # 6. Combined Stress Factor
    if risk_score > 50 and humidity > 80:
        risk_score += 10
        reasons.append("Combined stress: Heat + High humidity increases disease risk")

    # Final Result Mapping
    if risk_score >= 70:
        risk, loss, advice = "CRITICAL", "70-90%", "IMMEDIATE ACTION REQUIRED: Apply emergency irrigation, fungicides, and monitor field constantly. Consider late sowing if season permits."
    elif risk_score >= 45:
        risk, loss, advice = "HIGH RISK", "40-60%", "Take precautionary measures: Adjust irrigation schedule, apply pest control, add missing nutrients. Field needs attention within 48 hours."
    elif risk_score >= 25:
        risk, loss, advice = "MODERATE", "15-30%", "Field conditions are okay but could improve. Follow recommended practices and monitor weather changes."
    else:
        risk, loss, advice = "OPTIMAL", "0-10%", "Excellent conditions! Continue current management practices. Field health is optimal - expect good yield."

    # Add category-specific advice
    category_advice = {
        "Cereal": "Focus on nitrogen management and timely irrigation.",
        "Pulse": "Inoculate seeds with rhizobium culture for nitrogen fixation.",
        "Oilseed": "Ensure proper drainage to prevent waterlogging.",
        "Vegetable": "Regular harvesting and pest monitoring essential.",
        "Fruit": "Pruning and training needed for better yield.",
        "Spice": "Shade management important for quality produce.",
        "Commercial": "Follow integrated pest management (IPM) practices.",
        "Fodder": "Cut at right stage for maximum nutrition."
    }
    
    final_notes = f"Crop Category: {limits['category']}. " + category_advice.get(limits['category'], "")

    return {
        "risk_level": risk,
        "estimated_loss": loss,
        "disease_alert": disease_warning,
        "action_plan": advice,
        "analysis_notes": ". ".join(reasons) if reasons else "All parameters within optimal range",
        "recommendations": recommendations,
        "crop_category": limits['category'],
        "optimal_parameters": {
            "rainfall": f"{limits['min_rain']}-500mm",
            "temperature": f"{limits['max_temp']-15}-{limits['max_temp']}C",
            "humidity": f"{limits['min_humidity']}-90%",
            "soil_ph": limits['ideal_ph']
        }
    }
