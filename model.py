def predict_crop_high_level(rainfall, temperature, humidity, soil_ph, crop_type):
    # Professional projects use data structures to define "Optimal Zones"
    crop_thresholds = {
        "Rice": {"min_rain": 150, "max_temp": 35, "ideal_ph": 6.0},
        "Wheat": {"min_rain": 50, "max_temp": 25, "ideal_ph": 6.5},
        "Sugarcane": {"min_rain": 200, "max_temp": 40, "ideal_ph": 7.0},
        "Maize": {"min_rain": 60, "max_temp": 32, "ideal_ph": 6.2}
    }

    # Default to Rice if crop not found
    limits = crop_thresholds.get(crop_type, crop_thresholds["Rice"])
    
    risk_score = 0
    reasons = []

    # 1. Dynamic Rainfall Analysis
    if rainfall < limits["min_rain"]:
        risk_score += 35
        reasons.append(f"Low rainfall for {crop_type}")
    
    # 2. Dynamic Temperature Analysis
    if temperature > limits["max_temp"]:
        risk_score += 30
        reasons.append("Heat stress detected")

    # 3. Soil pH Health Check (The "Big Level" Addition)
    ph_diff = abs(soil_ph - limits["ideal_ph"])
    if ph_diff > 1.5:
        risk_score += 20
        reasons.append("Soil acidity/alkalinity imbalance")

    # 4. Humidity-Pathogen Logic
    disease_warning = "Clear"
    if humidity > 85 and temperature > 24:
        risk_score += 25
        disease_warning = "High Probability of Fungal Blight"

    # Final Result Mapping
    if risk_score >= 65:
        risk, loss, advice = "Critical", 80, "Emergency: Apply life-saving irrigation & bio-pesticides."
    elif risk_score >= 35:
        risk, loss, advice = "Warning", 40, "Precaution: Adjust fertilizer and check for pests."
    else:
        risk, loss, advice = "Optimal", 5, "Maintain current schedule. Field health is excellent."

    return {
        "risk_level": risk,
        "estimated_loss": f"{loss}%",
        "disease_alert": disease_warning,
        "action_plan": advice,
        "analysis_notes": ", ".join(reasons) if reasons else "All parameters within range"
    }