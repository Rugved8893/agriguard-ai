def predict_crop_loss(rainfall, temperature):
    if rainfall < 50 and temperature > 35:
        return "High Risk", 70
    elif rainfall < 100:
        return "Medium Risk", 40
    else:
        return "Low Risk", 10