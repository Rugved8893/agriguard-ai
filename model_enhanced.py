"""
Enhanced Crop Prediction Model for AgriGuard AI
More accurate analysis using comprehensive crop parameters, disease patterns, and environmental factors
"""

import random
from datetime import datetime

class CropPredictor:
    """Enhanced crop risk prediction with comprehensive analysis"""
    
    def __init__(self):
        self.crop_database = self._build_crop_database()
        self.disease_database = self._build_disease_database()
        self.season_data = self._get_season_data()
        
    def _build_crop_database(self):
        """Comprehensive crop database with optimal and tolerance ranges"""
        return {
            # CEREALS
            "Rice": {
                "category": "Cereal", "season": "Kharif",
                "optimal": {"rainfall_mm": (150, 250), "temp_c": (20, 30), "humidity": (70, 90), "ph": (5.5, 7.0)},
                "tolerance": {"rainfall_mm": (100, 300), "temp_c": (15, 35), "humidity": (60, 95), "ph": (5.0, 8.0)},
                "water_need": "High", "nutrient_need": "High N",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "Nov-Dec"},
                "common_diseases": ["Blast", "Bacterial Leaf Blight", "Brown Spot", "Sheath Blight"],
                "yield_optimal": {"min": 3, "max": 6, "unit": "tonnes/acre"},
                "regional_suitability": ["Punjab", "West Bengal", "Tamil Nadu", "Andhra Pradesh", "Karnataka"]
            },
            "Wheat": {
                "category": "Cereal", "season": "Rabi",
                "optimal": {"rainfall_mm": (50, 120), "temp_c": (15, 25), "humidity": (40, 70), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (25, 150), "temp_c": (10, 30), "humidity": (30, 80), "ph": (5.5, 8.0)},
                "water_need": "Medium", "nutrient_need": "High NPK",
                "growth_stages": {"sowing": "Oct-Nov", "harvest": "Mar-Apr"},
                "common_diseases": ["Rust", "Powdery Mildew", "Karnal Bunt", "Leaf Blight"],
                "yield_optimal": {"min": 2.5, "max": 4.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Punjab", "Haryana", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan"]
            },
            "Maize": {
                "category": "Cereal", "season": "Kharif/Rabi",
                "optimal": {"rainfall_mm": (60, 150), "temp_c": (22, 32), "humidity": (50, 80), "ph": (5.8, 7.0)},
                "tolerance": {"rainfall_mm": (40, 200), "temp_c": (18, 35), "humidity": (40, 90), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "High NPK",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "Oct-Nov"},
                "common_diseases": ["Leaf Blight", "Stalk Rot", "Curvularia Leaf Spot", "Maydis Leaf Blight"],
                "yield_optimal": {"min": 2.5, "max": 5, "unit": "tonnes/acre"},
                "regional_suitability": ["Karnataka", "Andhra Pradesh", "Maharashtra", "Madhya Pradesh", "Rajasthan"]
            },
            "Bajra": {
                "category": "Cereal", "season": "Kharif",
                "optimal": {"rainfall_mm": (40, 80), "temp_c": (25, 35), "humidity": (30, 60), "ph": (6.5, 8.0)},
                "tolerance": {"rainfall_mm": (20, 120), "temp_c": (20, 40), "humidity": (20, 80), "ph": (5.5, 8.5)},
                "water_need": "Low", "nutrient_need": "Medium",
                "growth_stages": {"sowing": "Jul-Aug", "harvest": "Oct-Nov"},
                "common_diseases": ["Downy Mildew", "Ergot", "Rust", "Leaf Spot"],
                "yield_optimal": {"min": 1.5, "max": 2.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Rajasthan", "Gujarat", "Maharashtra", "Haryana", "Uttar Pradesh"]
            },
            "Jowar": {
                "category": "Cereal", "season": "Kharif/Rabi",
                "optimal": {"rainfall_mm": (45, 100), "temp_c": (25, 35), "humidity": (35, 70), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (20, 40), "humidity": (25, 85), "ph": (5.5, 8.0)},
                "water_need": "Low-Medium", "nutrient_need": "Medium",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "Sep-Nov"},
                "common_diseases": ["Grain Mold", "Leaf Blight", "Stem Borer", "Anthracnose"],
                "yield_optimal": {"min": 1.5, "max": 3, "unit": "tonnes/acre"},
                "regional_suitability": ["Maharashtra", "Karnataka", "Andhra Pradesh", "Tamil Nadu", "Madhya Pradesh"]
            },
            "Ragi": {
                "category": "Cereal", "season": "Kharif",
                "optimal": {"rainfall_mm": (50, 120), "temp_c": (20, 30), "humidity": (50, 80), "ph": (5.5, 7.0)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (15, 35), "humidity": (40, 90), "ph": (5.0, 7.5)},
                "water_need": "Low-Medium", "nutrient_need": "Low-Medium",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "Nov-Dec"},
                "common_diseases": ["Finger Millet Blast", "Leaf Spot", "Brown Spot", "Foot Rot"],
                "yield_optimal": {"min": 1.5, "max": 2.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Karnataka", "Tamil Nadu", "Andhra Pradesh", "Odisha", "Maharashtra"]
            },
            
            # PULSES
            "Gram": {
                "category": "Pulse", "season": "Rabi",
                "optimal": {"rainfall_mm": (40, 80), "temp_c": (20, 30), "humidity": (35, 60), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (25, 100), "temp_c": (15, 35), "humidity": (25, 75), "ph": (5.5, 8.0)},
                "water_need": "Low-Medium", "nutrient_need": "Low (N-fixing)",
                "growth_stages": {"sowing": "Oct-Nov", "harvest": "Feb-Mar"},
                "common_diseases": ["Ascochyta Blight", "Powdery Mildew", "Rust", "Wilt"],
                "yield_optimal": {"min": 1, "max": 2, "unit": "tonnes/acre"},
                "regional_suitability": ["Madhya Pradesh", "Rajasthan", "Maharashtra", "Uttar Pradesh", "Karnataka"]
            },
            "Tur": {
                "category": "Pulse", "season": "Kharif",
                "optimal": {"rainfall_mm": (60, 120), "temp_c": (22, 32), "humidity": (50, 70), "ph": (5.5, 7.0)},
                "tolerance": {"rainfall_mm": (40, 180), "temp_c": (18, 38), "humidity": (35, 85), "ph": (5.0, 7.5)},
                "water_need": "Medium", "nutrient_need": "Low (N-fixing)",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "Nov-Feb"},
                "common_diseases": ["Powdery Mildew", "Phytophthora Blight", "Sterility Mosaic", "Wilt"],
                "yield_optimal": {"min": 1.5, "max": 2.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Maharashtra", "Karnataka", "Andhra Pradesh", "Gujarat", "Madhya Pradesh"]
            },
            "Moong": {
                "category": "Pulse", "season": "Kharif/Rabi",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (25, 35), "humidity": (40, 70), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (20, 40), "humidity": (30, 85), "ph": (5.5, 8.0)},
                "water_need": "Low-Medium", "nutrient_need": "Low",
                "growth_stages": {"sowing": "Jun-Jul/Sep-Oct", "harvest": "Sep-Oct/Dec-Jan"},
                "common_diseases": ["Yellow Mosaic Virus", "Powdery Mildew", "Anthracnose", "Leaf Spot"],
                "yield_optimal": {"min": 0.8, "max": 1.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Rajasthan", "Maharashtra", "Karnataka", "Andhra Pradesh", "Tamil Nadu"]
            },
            
            # OILSEEDS
            "Groundnut": {
                "category": "Oilseed", "season": "Kharif/Rabi",
                "optimal": {"rainfall_mm": (50, 120), "temp_c": (24, 32), "humidity": (40, 70), "ph": (5.5, 7.0)},
                "tolerance": {"rainfall_mm": (30, 180), "temp_c": (20, 38), "humidity": (30, 85), "ph": (5.0, 7.5)},
                "water_need": "Medium", "nutrient_need": "Medium-High",
                "growth_stages": {"sowing": "Jun-Jul/Oct-Nov", "harvest": "Oct-Nov/Feb-Mar"},
                "common_diseases": ["Leaf Spot", "Rust", "Collar Rot", "Aspergillus Crown Rot"],
                "yield_optimal": {"min": 1.5, "max": 2.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Gujarat", "Andhra Pradesh", "Karnataka", "Tamil Nadu", "Maharashtra"]
            },
            "Mustard": {
                "category": "Oilseed", "season": "Rabi",
                "optimal": {"rainfall_mm": (40, 80), "temp_c": (15, 25), "humidity": (35, 65), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (20, 120), "temp_c": (10, 32), "humidity": (25, 80), "ph": (5.5, 8.0)},
                "water_need": "Low-Medium", "nutrient_need": "Medium",
                "growth_stages": {"sowing": "Oct-Nov", "harvest": "Feb-Mar"},
                "common_diseases": ["White Rust", "Alternaria Blight", "Powdery Mildew", "Downy Mildew"],
                "yield_optimal": {"min": 1, "max": 1.8, "unit": "tonnes/acre"},
                "regional_suitability": ["Rajasthan", "Uttar Pradesh", "Madhya Pradesh", "Haryana", "Gujarat"]
            },
            "Soybean": {
                "category": "Oilseed", "season": "Kharif",
                "optimal": {"rainfall_mm": (60, 120), "temp_c": (20, 32), "humidity": (50, 70), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (40, 180), "temp_c": (15, 38), "humidity": (35, 85), "ph": (5.5, 7.5)},
                "water_need": "Medium", "nutrient_need": "Medium-High",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "Sep-Oct"},
                "common_diseases": ["Yellow Mosaic Virus", "Bacterial Pustule", " Cercospora Leaf Spot", "Stem Rot"],
                "yield_optimal": {"min": 1.5, "max": 2.5, "unit": "tonnes/acre"},
                "regional_suitability": ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Karnataka", "Gujarat"]
            },
            "Sunflower": {
                "category": "Oilseed", "season": "Kharif/Rabi",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (20, 30), "humidity": (45, 70), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (15, 35), "humidity": (35, 85), "ph": (5.5, 8.0)},
                "water_need": "Medium", "nutrient_need": "Medium-High",
                "growth_stages": {"sowing": "Jun-Jul/Oct-Nov", "harvest": "Sep-Oct/Jan-Feb"},
                "common_diseases": ["Alternaria Leaf Spot", "Powdery Mildew", "Rust", "Head Rot"],
                "yield_optimal": {"min": 1, "max": 1.8, "unit": "tonnes/acre"},
                "regional_suitability": ["Karnataka", "Maharashtra", "Andhra Pradesh", "Tamil Nadu", "Madhya Pradesh"]
            },
            
            # CASH CROPS
            "Sugarcane": {
                "category": "Cash Crop", "season": "Annual",
                "optimal": {"rainfall_mm": (200, 300), "temp_c": (24, 34), "humidity": (70, 85), "ph": (6.5, 7.5)},
                "tolerance": {"rainfall_mm": (150, 400), "temp_c": (18, 40), "humidity": (50, 95), "ph": (6.0, 8.0)},
                "water_need": "Very High", "nutrient_need": "Very High NPK",
                "growth_stages": {"sowing": "Feb-Mar/Oct-Nov", "harvest": "12-18 months"},
                "common_diseases": ["Red Rot", "Smut", "Pokkah Boeng", "Leaf Scald"],
                "yield_optimal": {"min": 40, "max": 70, "unit": "tonnes/acre"},
                "regional_suitability": ["Uttar Pradesh", "Maharashtra", "Karnataka", "Tamil Nadu", "Andhra Pradesh"]
            },
            "Cotton": {
                "category": "Cash Crop", "season": "Kharif",
                "optimal": {"rainfall_mm": (60, 120), "temp_c": (25, 35), "humidity": (50, 70), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (40, 180), "temp_c": (18, 42), "humidity": (35, 85), "ph": (5.5, 8.0)},
                "water_need": "Medium-High", "nutrient_need": "High NPK",
                "growth_stages": {"sowing": "May-Jun", "harvest": "Sep-Dec"},
                "common_diseases": ["Bacterial Blight", "Cotton Wilt", "Leaf Curl Virus", "Boll Rot"],
                "yield_optimal": {"min": 1.5, "max": 3, "unit": "quintals/acre"},
                "regional_suitability": ["Gujarat", "Maharashtra", "Andhra Pradesh", "Punjab", "Haryana"]
            },
            
            # VEGETABLES
            "Tomato": {
                "category": "Vegetable", "season": "Rabi/Kharif",
                "optimal": {"rainfall_mm": (60, 120), "temp_c": (20, 28), "humidity": (60, 80), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (40, 180), "temp_c": (15, 35), "humidity": (50, 90), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "High NPK",
                "growth_stages": {"sowing": "Jun-Jul/Oct-Nov", "harvest": "90-120 days"},
                "common_diseases": ["Late Blight", "Early Blight", "Bacterial Wilt", "Tomato Leaf Curl"],
                "yield_optimal": {"min": 10, "max": 20, "unit": "tonnes/acre"},
                "regional_suitability": ["Andhra Pradesh", "Karnataka", "Maharashtra", "Orissa", "West Bengal"]
            },
            "Potato": {
                "category": "Vegetable", "season": "Rabi",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (15, 25), "humidity": (60, 80), "ph": (5.5, 6.5)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (10, 30), "humidity": (50, 90), "ph": (5.0, 7.0)},
                "water_need": "Medium", "nutrient_need": "High NPK",
                "growth_stages": {"sowing": "Oct-Nov", "harvest": "90-120 days"},
                "common_diseases": ["Late Blight", "Early Blight", "Black Scurf", "Bacterial Wilt"],
                "yield_optimal": {"min": 8, "max": 15, "unit": "tonnes/acre"},
                "regional_suitability": ["Uttar Pradesh", "West Bengal", "Punjab", "Bihar", "Gujarat"]
            },
            "Onion": {
                "category": "Vegetable", "season": "Rabi/Kharif",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (20, 30), "humidity": (50, 70), "ph": (6.0, 7.5)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (15, 35), "humidity": (40, 85), "ph": (5.5, 8.0)},
                "water_need": "Medium", "nutrient_need": "Medium-High",
                "growth_stages": {"sowing": "Sep-Nov/May-Jun", "harvest": "90-150 days"},
                "common_diseases": ["Purple Blotch", "Stemphylium Blight", "Onion Thrips", "Neck Rot"],
                "yield_optimal": {"min": 8, "max": 15, "unit": "tonnes/acre"},
                "regional_suitability": ["Maharashtra", "Gujarat", "Karnataka", "Tamil Nadu", "Andhra Pradesh"]
            },
            "Cabbage": {
                "category": "Vegetable", "season": "Rabi",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (15, 22), "humidity": (70, 85), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (10, 28), "humidity": (60, 95), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "High N",
                "growth_stages": {"sowing": "Sep-Nov", "harvest": "70-120 days"},
                "common_diseases": ["Black Rot", "Club Root", "Downy Mildew", "Aphids"],
                "yield_optimal": {"min": 20, "max": 40, "unit": "tonnes/acre"},
                "regional_suitability": ["West Bengal", "Odisha", "Uttar Pradesh", "Maharashtra", "Karnataka"]
            },
            "Cauliflower": {
                "category": "Vegetable", "season": "Rabi",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (15, 22), "humidity": (70, 85), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (10, 28), "humidity": (60, 95), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "High N",
                "growth_stages": {"sowing": "Sep-Nov", "harvest": "65-90 days"},
                "common_diseases": ["Black Rot", "Club Root", "Downy Mildew", "Stalk Rot"],
                "yield_optimal": {"min": 15, "max": 30, "unit": "tonnes/acre"},
                "regional_suitability": ["West Bengal", "Odisha", "Uttar Pradesh", "Maharashtra", "Karnataka"]
            },
            "Carrot": {
                "category": "Vegetable", "season": "Rabi",
                "optimal": {"rainfall_mm": (40, 80), "temp_c": (18, 26), "humidity": (60, 75), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (25, 120), "temp_c": (10, 32), "humidity": (50, 85), "ph": (5.5, 7.5)},
                "water_need": "Medium", "nutrient_need": "Medium",
                "growth_stages": {"sowing": "Sep-Nov", "harvest": "90-120 days"},
                "common_diseases": ["Leaf Blight", "Cavity Spot", "Root Knot", "Aphids"],
                "yield_optimal": {"min": 8, "max": 15, "unit": "tonnes/acre"},
                "regional_suitability": ["West Bengal", "Andhra Pradesh", "Karnataka", "Tamil Nadu", "Maharashtra"]
            },
            "Brinjal": {
                "category": "Vegetable", "season": "Kharif/Rabi",
                "optimal": {"rainfall_mm": (60, 120), "temp_c": (24, 32), "humidity": (60, 75), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (40, 180), "temp_c": (18, 38), "humidity": (50, 85), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "Medium-High",
                "growth_stages": {"sowing": "Jun-Jul/Oct-Nov", "harvest": "90-120 days"},
                "common_diseases": ["Phytophthora Blight", "Bacterial Wilt", "Fruit Borer", "Shoot Borer"],
                "yield_optimal": {"min": 15, "max": 25, "unit": "tonnes/acre"},
                "regional_suitability": ["West Bengal", "Odisha", "Andhra Pradesh", "Karnataka", "Maharashtra"]
            },
            "Okra": {
                "category": "Vegetable", "season": "Kharif",
                "optimal": {"rainfall_mm": (60, 120), "temp_c": (25, 35), "humidity": (60, 80), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (40, 180), "temp_c": (20, 40), "humidity": (50, 90), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "Medium",
                "growth_stages": {"sowing": "Jun-Jul", "harvest": "45-60 days"},
                "common_diseases": ["Yellow Vein Mosaic", "Powdery Mildew", "Fruit Borer", "Damping Off"],
                "yield_optimal": {"min": 6, "max": 12, "unit": "tonnes/acre"},
                "regional_suitability": ["West Bengal", "Gujarat", "Maharashtra", "Andhra Pradesh", "Tamil Nadu"]
            },
            
            # FRUITS
            "Mango": {
                "category": "Fruit", "season": "Summer",
                "optimal": {"rainfall_mm": (100, 200), "temp_c": (24, 32), "humidity": (50, 70), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (50, 300), "temp_c": (18, 42), "humidity": (35, 85), "ph": (5.5, 7.5)},
                "water_need": "Medium", "nutrient_need": "Medium-High",
                "growth_stages": {"flowering": "Jan-Feb", "harvest": "Apr-Jul"},
                "common_diseases": ["Anthracnose", "Powdery Mildew", "Mango Hopper", "Fruit Fly"],
                "yield_optimal": {"min": 5, "max": 15, "unit": "tonnes/acre"},
                "regional_suitability": ["Uttar Pradesh", "Andhra Pradesh", "Karnataka", "Tamil Nadu", "Gujarat"]
            },
            "Banana": {
                "category": "Fruit", "season": "Year-round",
                "optimal": {"rainfall_mm": (150, 250), "temp_c": (26, 32), "humidity": (70, 85), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (100, 400), "temp_c": (18, 38), "humidity": (50, 95), "ph": (5.5, 7.5)},
                "water_need": "Very High", "nutrient_need": "Very High",
                "growth_stages": {"planting": "Mar-May/Sep-Nov", "harvest": "9-12 months"},
                "common_diseases": ["Panama Wilt", "Sigatoka Leaf Spot", "Bunchy Top", "Crown Rot"],
                "yield_optimal": {"min": 20, "max": 40, "unit": "tonnes/acre"},
                "regional_suitability": ["Maharashtra", "Tamil Nadu", "Karnataka", "Andhra Pradesh", "Gujarat"]
            },
            "Papaya": {
                "category": "Fruit", "season": "Year-round",
                "optimal": {"rainfall_mm": (100, 200), "temp_c": (24, 32), "humidity": (60, 75), "ph": (6.0, 7.0)},
                "tolerance": {"rainfall_mm": (50, 300), "temp_c": (18, 38), "humidity": (45, 90), "ph": (5.5, 7.5)},
                "water_need": "Medium-High", "nutrient_need": "Medium-High",
                "growth_stages": {"planting": "Feb-Apr/Aug-Oct", "harvest": "8-12 months"},
                "common_diseases": ["Papaya Ring Spot", "Anthracnose", "Powdery Mildew", "Stem Rot"],
                "yield_optimal": {"min": 30, "max": 60, "unit": "tonnes/acre"},
                "regional_suitability": ["Andhra Pradesh", "Karnataka", "Maharashtra", "Tamil Nadu", "West Bengal"]
            },
            "Guava": {
                "category": "Fruit", "season": "Winter",
                "optimal": {"rainfall_mm": (100, 180), "temp_c": (23, 32), "humidity": (50, 70), "ph": (6.5, 7.5)},
                "tolerance": {"rainfall_mm": (50, 250), "temp_c": (18, 38), "humidity": (40, 85), "ph": (5.5, 8.0)},
                "water_need": "Medium", "nutrient_need": "Medium",
                "growth_stages": {"flowering": "Jun-Sep", "harvest": "Nov-Mar"},
                "common_diseases": ["Anthracnose", "Fruit Fly", "Guava Wilt", "Cercospora Leaf Spot"],
                "yield_optimal": {"min": 8, "max": 20, "unit": "tonnes/acre"},
                "regional_suitability": ["Uttar Pradesh", "Madhya Pradesh", "Maharashtra", "Andhra Pradesh", "Karnataka"]
            },
            "Pomegranate": {
                "category": "Fruit", "season": "Winter",
                "optimal": {"rainfall_mm": (50, 120), "temp_c": (25, 35), "humidity": (40, 60), "ph": (6.5, 7.5)},
                "tolerance": {"rainfall_mm": (30, 200), "temp_c": (18, 42), "humidity": (30, 80), "ph": (5.5, 8.0)},
                "water_need": "Low-Medium", "nutrient_need": "Medium",
                "growth_stages": {"flowering": "Mar-May", "harvest": "Sep-Dec"},
                "common_diseases": ["Bacterial Blight", "Leaf Spot", "Fruit Borer", "Anar Butterfly"],
                "yield_optimal": {"min": 8, "max": 15, "unit": "tonnes/acre"},
                "regional_suitability": ["Maharashtra", "Gujarat", "Karnataka", "Andhra Pradesh", "Tamil Nadu"]
            },
            "Grapes": {
                "category": "Fruit", "season": "Summer",
                "optimal": {"rainfall_mm": (50, 100), "temp_c": (24, 32), "humidity": (50, 70), "ph": (6.5, 7.5)},
                "tolerance": {"rainfall_mm": (30, 150), "temp_c": (18, 38), "humidity": (40, 85), "ph": (6.0, 8.0)},
                "water_need": "Medium-High", "nutrient_need": "High",
                "growth_stages": {"pruning": "Apr-May/Oct-Nov", "harvest": "Jun-Sep/Dec-Mar"},
                "common_diseases": ["Downy Mildew", "Powdery Mildew", "Anthracnose", "Grape Berry Moth"],
                "yield_optimal": {"min": 8, "max": 15, "unit": "tonnes/acre"},
                "regional_suitability": ["Maharashtra", "Karnataka", "Tamil Nadu", "Andhra Pradesh", "Madhya Pradesh"]
            },
        }
    
    def _build_disease_database(self):
        """Comprehensive disease database with conditions and treatments"""
        return {
            "Blast": {
                "crops": ["Rice", "Ragi"],
                "conditions": {"temp": (20, 30), "humidity": (80, 100), "rain": "High"},
                "severity": "High", "type": "Fungal",
                "symptoms": "Diamond-shaped lesions with gray centers on leaves",
                "treatment": {"chemical": "Tricyclazole 75% WP @ 0.6 g/L or Isoprothiolane", "organic": "Neem oil 5ml/L, remove infected leaves"},
                "prevention": "Use resistant varieties, avoid excessive N fertilizer, maintain proper spacing"
            },
            "Rust": {
                "crops": ["Wheat", "Groundnut", "Mustard", "Bajra"],
                "conditions": {"temp": (15, 25), "humidity": (70, 90), "rain": "Moderate"},
                "severity": "High", "type": "Fungal",
                "symptoms": "Orange-brown pustules on leaves and stems",
                "treatment": {"chemical": "Propiconazole 25% EC @ 1 ml/L or Mancozeb", "organic": "Baking soda spray, sulfur dust"},
                "prevention": "Use resistant varieties, early sowing, remove crop residues"
            },
            "Bacterial Leaf Blight": {
                "crops": ["Rice"],
                "conditions": {"temp": (25, 34), "humidity": (80, 100), "rain": "High"},
                "severity": "High", "type": "Bacterial",
                "symptoms": "Yellow to white lesions starting from leaf tips, bacterial ooze",
                "treatment": {"chemical": "Copper Oxychloride 50% WP @ 2.5 g/L", "organic": "Neem extract, biocontrol agents"},
                "prevention": "Use certified seeds, avoid working in wet fields, crop rotation"
            },
            "Powdery Mildew": {
                "crops": ["Wheat", "Gram", "Moong", "Peas", "Grapes"],
                "conditions": {"temp": (20, 30), "humidity": (50, 70), "rain": "Low"},
                "severity": "Moderate", "type": "Fungal",
                "symptoms": "White powdery coating on leaves, stems, and fruits",
                "treatment": {"chemical": "Sulfur 80% WDG @ 2 g/L or Carbendazim", "organic": "Neem oil, milk spray (1:9 ratio)"},
                "prevention": "Adequate spacing, avoid excess nitrogen, resistant varieties"
            },
            "Wilts": {
                "crops": ["Gram", "Tur", "Cotton", "Banana", "Brinjal"],
                "conditions": {"temp": (25, 35), "humidity": (60, 80), "rain": "Moderate"},
                "severity": "High", "type": "Fungal/Bacterial",
                "symptoms": "Wilting despite adequate water, yellowing, vascular discoloration",
                "treatment": {"chemical": "Carbendazim 50% WP or Trichoderma viride", "organic": "Neem cake, biocontrol"},
                "prevention": "Use resistant varieties, crop rotation, solarization, avoid waterlogging"
            },
            "Leaf Spot": {
                "crops": ["Rice", "Maize", "Groundnut", "Cotton", "Tomato"],
                "conditions": {"temp": (25, 32), "humidity": (70, 90), "rain": "Moderate-High"},
                "severity": "Moderate", "type": "Fungal",
                "symptoms": "Brown to black spots on leaves, may have yellow halos",
                "treatment": {"chemical": "Mancozeb 75% WP @ 2.5 g/L or Chlorothalonil", "organic": "Neem extract, garlic extract"},
                "prevention": "Remove infected debris, adequate spacing, avoid overhead irrigation"
            },
            "Yellow Mosaic Virus": {
                "crops": ["Moong", "Urhad", "Soybean", "Tomato"],
                "conditions": {"temp": (25, 35), "humidity": (60, 80), "rain": "Moderate"},
                "severity": "High", "type": "Viral",
                "symptoms": "Yellow mottling and mosaic patterns on leaves, stunted growth",
                "treatment": {"chemical": "No direct treatment - control vectors", "organic": "Neem oil to repel vectors"},
                "prevention": "Use resistant varieties, control whiteflies/jassids, early sowing"
            },
            "Late Blight": {
                "crops": ["Potato", "Tomato"],
                "conditions": {"temp": (15, 22), "humidity": (90, 100), "rain": "High"},
                "severity": "Very High", "type": "Fungal",
                "symptoms": "Water-soaked lesions turning brown, white mold on undersides",
                "treatment": {"chemical": "Metalaxyl + Mancozeb or Mancozeb alone", "organic": "Bordeaux mixture, remove infected plants"},
                "prevention": "Use resistant varieties, avoid overhead irrigation, proper spacing"
            },
            "Red Rot": {
                "crops": ["Sugarcane"],
                "conditions": {"temp": (25, 35), "humidity": (70, 90), "rain": "Moderate"},
                "severity": "High", "type": "Fungal",
                "symptoms": "Red stripes on leaves, internal pith shows red with white spots",
                "treatment": {"chemical": "Carbendazim or Thiophanate methyl", "organic": "Heat treatment of seed sets"},
                "prevention": "Use healthy seed, crop rotation, resistant varieties"
            },
            "Cotton Wilt": {
                "crops": ["Cotton"],
                "conditions": {"temp": (28, 38), "humidity": (60, 80), "rain": "Moderate"},
                "severity": "High", "type": "Fungal",
                "symptoms": "Wilting, yellowing starting from lower leaves, brown vascular tissue",
                "treatment": {"chemical": "Carbendazim or Trichoderma", "organic": "Neem cake, biofertilizers"},
                "prevention": "Use resistant varieties, crop rotation with legumes, avoid Monoculture"
            },
            "Mango Hopper": {
                "crops": ["Mango"],
                "conditions": {"temp": (25, 35), "humidity": (60, 80), "rain": "Moderate"},
                "severity": "High", "type": "Insect",
                "symptoms": "Hoppers on buds/leaves, honeydew sooty mold, flower dropping",
                "treatment": {"chemical": "Imidacloprid 17.8% SL or Cyantraniliprole", "organic": "Neem oil, yellow sticky traps"},
                "prevention": "Monitoring, early morning spray, destroy fallen fruits"
            },
            "Fruit Fly": {
                "crops": ["Mango", "Guava", "Citrus", "Melon"],
                "conditions": {"temp": (25, 35), "humidity": (60, 80), "rain": "Low-Moderate"},
                "severity": "High", "type": "Insect",
                "symptoms": "Fruit damage, Maggots inside fruits, rotting",
                "treatment": {"chemical": "Malathion 50% EC + sugar, protein hydrolysate", "organic": "Cuelure traps, bagging fruits"},
                "prevention": "Orchard sanitation, early harvesting, male annihilation technique"
            },
        }
    
    def _get_season_data(self):
        """Get current season and its characteristics"""
        month = datetime.now().month
        if month in [6, 7, 8, 9]:
            return {"season": "Kharif", "monsoon": True, "rain_likely": True}
        elif month in [10, 11, 12, 1, 2, 3]:
            return {"season": "Rabi", "monsoon": False, "rain_likely": False}
        else:
            return {"season": "Zaid", "monsoon": False, "rain_likely": False}
    
    def predict(self, rainfall, temperature, humidity, soil_ph, crop_type):
        """Main prediction function with comprehensive analysis"""
        
        # Get crop data or use defaults
        crop_data = self.crop_database.get(crop_type, self.crop_database["Rice"])
        
        # Calculate individual risk factors
        risks = self._calculate_risks(rainfall, temperature, humidity, soil_ph, crop_data)
        
        # Determine disease risks
        disease_risks = self._calculate_disease_risk(temperature, humidity, crop_type, crop_data)
        
        # Calculate overall risk score - extract score values from each risk dictionary
        total_risk = sum(risk["score"] for risk in risks.values())
        
        # Determine risk level and recommendations
        risk_level, loss_estimate, action_plan = self._get_risk_assessment(total_risk, risks)
        
        # Get optimal parameters for this crop
        optimal = crop_data["optimal"]
        
        return {
            "risk_level": risk_level,
            "estimated_loss": loss_estimate,
            "disease_alert": disease_risks["alert"],
            "action_plan": action_plan,
            "analysis_notes": self._generate_notes(risks, crop_data),
            "recommendations": self._generate_recommendations(risks, disease_risks, crop_data),
            "crop_category": crop_data["category"],
            "season": crop_data["season"],
            "water_need": crop_data["water_need"],
            "nutrient_need": crop_data["nutrient_need"],
            "optimal_parameters": {
                "rainfall": f"{optimal['rainfall_mm'][0]}-{optimal['rainfall_mm'][1]}mm",
                "temperature": f"{optimal['temp_c'][0]}-{optimal['temp_c'][1]}°C",
                "humidity": f"{optimal['humidity'][0]}-{optimal['humidity'][1]}%",
                "soil_ph": f"{optimal['ph'][0]}-{optimal['ph'][1]}"
            },
            "expected_yield": f"{crop_data['yield_optimal']['min']}-{crop_data['yield_optimal']['max']} {crop_data['yield_optimal']['unit']}",
            "common_diseases": crop_data["common_diseases"],
            "suitable_regions": crop_data["regional_suitability"][:3],
            "detailed_risks": risks,
            "disease_details": disease_risks["details"]
        }
    
    def _calculate_risks(self, rainfall, temperature, humidity, soil_ph, crop_data):
        """Calculate individual risk factors"""
        risks = {}
        opt = crop_data["optimal"]
        tol = crop_data["tolerance"]
        
        # 1. Rainfall Risk
        rain_risk = 0
        rain_reason = ""
        if rainfall < opt["rainfall_mm"][0]:
            deficit = opt["rainfall_mm"][0] - rainfall
            if deficit > 100:
                rain_risk = 25
                rain_reason = f"Critical water shortage - need {opt['rainfall_mm'][0]}mm minimum"
            elif deficit > 50:
                rain_risk = 15
                rain_reason = f"Water deficit - below optimal range"
            else:
                rain_risk = 8
                rain_reason = "Slightly below optimal rainfall"
        elif rainfall > opt["rainfall_mm"][1]:
            excess = rainfall - opt["rainfall_mm"][1]
            if excess > 100:
                rain_risk = 20
                rain_reason = f"Excessive rainfall - risk of waterlogging"
            else:
                rain_risk = 10
                rain_reason = "Above optimal rainfall"
        
        if rain_risk == 0:
            rain_reason = "Rainfall within optimal range"
        risks["rainfall"] = {"score": rain_risk, "reason": rain_reason, "value": rainfall}
        
        # 2. Temperature Risk
        temp_risk = 0
        temp_reason = ""
        if temperature < opt["temp_c"][0]:
            if temperature < opt["temp_c"][0] - 10:
                temp_risk = 20
                temp_reason = f"Cold stress - temperature too low for {crop_data['category']}"
            else:
                temp_risk = 10
                temp_reason = "Temperature below optimal range"
        elif temperature > opt["temp_c"][1]:
            if temperature > opt["temp_c"][1] + 8:
                temp_risk = 25
                temp_reason = f"Extreme heat stress - severe impact on crop"
            elif temperature > opt["temp_c"][1] + 5:
                temp_risk = 18
                temp_reason = "High temperature - heat stress conditions"
            else:
                temp_risk = 10
                temp_reason = "Temperature above optimal range"
        
        if temp_risk == 0:
            temp_reason = "Temperature within optimal range"
        risks["temperature"] = {"score": temp_risk, "reason": temp_reason, "value": temperature}
        
        # 3. Humidity Risk
        hum_risk = 0
        hum_reason = ""
        if humidity < opt["humidity"][0]:
            if humidity < opt["humidity"][0] - 20:
                hum_risk = 15
                hum_reason = "Very low humidity - moisture stress"
            else:
                hum_risk = 8
                hum_reason = "Humidity below optimal"
        elif humidity > opt["humidity"][1]:
            if humidity > 90:
                hum_risk = 15
                hum_reason = "Very high humidity - disease risk"
            else:
                hum_risk = 8
                hum_reason = "Humidity above optimal"
        
        if hum_risk == 0:
            hum_reason = "Humidity within optimal range"
        risks["humidity"] = {"score": hum_risk, "reason": hum_reason, "value": humidity}
        
        # 4. Soil pH Risk
        ph_risk = 0
        ph_reason = ""
        ideal_ph = (opt["ph"][0] + opt["ph"][1]) / 2
        ph_diff = soil_ph - ideal_ph
        
        if abs(ph_diff) > 2.0:
            ph_risk = 20
            ph_reason = f"Soil pH {soil_ph} severely outside optimal range"
        elif abs(ph_diff) > 1.0:
            ph_risk = 10
            ph_reason = f"Soil pH {soil_ph} slightly outside optimal"
        elif abs(ph_diff) > 0.5:
            ph_risk = 3
            pml_reason = "Minor pH deviation from optimal"
        
        if ph_risk == 0:
            ph_reason = "Soil pH within optimal range"
        risks["soil_ph"] = {"score": ph_risk, "reason": ph_reason, "value": soil_ph}
        
        return risks
    
    def _calculate_disease_risk(self, temperature, humidity, crop_type, crop_data):
        """Calculate disease risks based on conditions"""
        details = []
        alert = "Low Risk"
        
        # Check each common disease for this crop
        for disease_name in crop_data.get("common_diseases", []):
            disease = self.disease_database.get(disease_name)
            if not disease:
                continue
            
            # Check if conditions favor this disease
            cond = disease["conditions"]
            temp_range = cond.get("temp", (15, 30))
            hum_range = cond.get("humidity", (60, 80))
            
            temp_favors = temp_range[0] <= temperature <= temp_range[1]
            hum_favors = hum_range[0] <= humidity <= hum_range[1]
            
            if temp_favors and hum_favors:
                risk_score = 0
                if temp_favors:
                    risk_score += 40
                if hum_favors:
                    risk_score += 40
                
                # High humidity adds more risk
                if humidity > 85:
                    risk_score += 20
                
                details.append({
                    "disease": disease_name,
                    "risk_score": min(risk_score, 100),
                    "type": disease["type"],
                    "severity": disease["severity"],
                    "symptoms": disease["symptoms"],
                    "treatment": disease["treatment"]["chemical"],
                    "organic_treatment": disease["treatment"]["organic"],
                    "prevention": disease["prevention"]
                })
        
        # Sort by risk score
        details.sort(key=lambda x: x["risk_score"], reverse=True)
        
        if details:
            if details[0]["risk_score"] >= 70:
                alert = f"HIGH RISK: {details[0]['disease']} likely"
            elif details[0]["risk_score"] >= 40:
                alert = f"MODERATE RISK: Watch for {details[0]['disease']}"
            else:
                alert = "Low Risk - Monitor regularly"
        
        return {"alert": alert, "details": details}
    
    def _get_risk_assessment(self, total_risk, risks):
        """Determine overall risk level and action plan"""
        
        # Weight the risks - some are more critical
        weighted_risk = (
            risks["rainfall"]["score"] * 1.2 +
            risks["temperature"]["score"] * 1.3 +
            risks["humidity"]["score"] * 1.0 +
            risks["soil_ph"]["score"] * 0.8
        )
        
        if weighted_risk >= 70:
            return "CRITICAL", "70-90%", (
                "IMMEDIATE ACTION REQUIRED!\n\n"
                "- Apply emergency irrigation if rainfall is low\n"
                "- Apply preventive fungicides as conditions favor diseases\n"
                "- Use shade nets if temperature is extreme\n"
                "- Monitor field every 12 hours\n"
                "- Consider rescue operations if crop is severely stressed"
            )
        elif weighted_risk >= 45:
            return "HIGH RISK", "40-60%", (
                "TAKE PRECAUTIONARY MEASURES!\n\n"
                "- Adjust irrigation schedule immediately\n"
                "- Apply pest/disease preventive measures\n"
                "- Add missing nutrients (NPK balance)\n"
                "- Monitor field at least twice daily\n"
                "- Be prepared for intensive care within 48 hours"
            )
        elif weighted_risk >= 25:
            return "MODERATE", "15-30%", (
                "CONDITIONS NEED ATTENTION\n\n"
                "- Continue regular irrigation\n"
                "- Follow recommended fertilizer schedule\n"
                "- Monitor weather changes\n"
                "- Good conditions for preventive measures\n"
                "- Field should improve with normal care"
            )
        else:
            return "OPTIMAL", "0-10%", (
                "EXCELLENT CONDITIONS!\n\n"
                "- All parameters within optimal range\n"
                "- Continue current management practices\n"
                "- Expect good to excellent yield\n"
                "- Field health is optimal\n"
                "- Focus on maintenance and harvesting"
            )
    
    def _generate_notes(self, risks, crop_data):
        """Generate analysis notes"""
        notes = []
        
        for factor, data in risks.items():
            if data["score"] > 0:
                notes.append(f"{factor.capitalize()}: {data['reason']}")
            else:
                notes.append(f"{factor.capitalize()}: Optimal - {data['reason']}")
        
        notes.append(f"Best season for {crop_data['category']}: {crop_data['season']}")
        
        return " | ".join(notes)
    
    def _generate_recommendations(self, risks, disease_risks, crop_data):
        """Generate specific recommendations"""
        recommendations = []
        
        # Weather-based recommendations
        if risks["rainfall"]["score"] > 10:
            if risks["rainfall"]["value"] < crop_data["optimal"]["rainfall_mm"][0]:
                recommendations.append(f"💧 Install drip irrigation - crop needs more water")
                recommendations.append(f"💧 Consider rainwater harvesting for supplemental irrigation")
            else:
                recommendations.append(f"💧 Improve drainage to prevent waterlogging")
        
        if risks["temperature"]["score"] > 10:
            recommendations.append(f"🌡️ Use mulching to regulate soil temperature")
            recommendations.append(f"🌡️ Provide shade nets during extreme heat")
        
        if risks["humidity"]["score"] > 10:
            recommendations.append(f"💨 Ensure proper air circulation between plants")
            recommendations.append(f"💨 Avoid overhead irrigation - use drip")
        
        if risks["soil_ph"]["score"] > 10:
            ph_val = risks["soil_ph"]["value"]
            if ph_val < 6.0:
                recommendations.append(f"🧪 Apply lime to raise soil pH")
            else:
                recommendations.append(f"🧪 Apply gypsum to lower soil pH")
        
        # Disease recommendations
        if disease_risks["details"]:
            top_disease = disease_risks["details"][0]
            if top_disease["risk_score"] >= 50:
                recommendations.append(f"🦠 Apply {top_disease['treatment']} for {top_disease['disease']}")
                recommendations.append(f"🦠 Prevention: {top_disease['prevention']}")
        
        # General recommendations
        recommendations.append(f"🌱 Follow {crop_data['nutrient_need']} nutrient management")
        recommendations.append(f"🌱 Water requirement: {crop_data['water_need']}")
        
        return recommendations


# Create instance for use
predictor = CropPredictor()

def predict_crop_high_level(rainfall, temperature, humidity, soil_ph, crop_type):
    """Enhanced prediction function that returns comprehensive results"""
    result = predictor.predict(rainfall, temperature, humidity, soil_ph, crop_type)
    
    # Add legacy support - flatten some fields for backward compatibility
    return {
        "risk_level": result["risk_level"],
        "estimated_loss": result["estimated_loss"],
        "disease_alert": result["disease_alert"],
        "action_plan": result["action_plan"],
        "analysis_notes": result["analysis_notes"],
        "recommendations": result["recommendations"],
        "crop_category": result["crop_category"],
        "season": result["season"],
        "optimal_parameters": result["optimal_parameters"],
        "expected_yield": result["expected_yield"],
        "common_diseases": result["common_diseases"],
        "suitable_regions": result["suitable_regions"],
        "water_need": result["water_need"],
        "nutrient_need": result["nutrient_need"],
        "detailed_risks": result["detailed_risks"],
        "disease_details": result["disease_details"]
    }


# Test the enhanced model
if __name__ == "__main__":
    # Test with sample data
    result = predict_crop_high_level(
        rainfall=150,
        temperature=28,
        humidity=75,
        soil_ph=6.5,
        crop_type="Rice"
    )
    
    print("=" * 60)
    print("ENHANCED CROP PREDICTION RESULTS")
    print("=" * 60)
    print(f"\n📊 Risk Level: {result['risk_level']}")
    print(f"📉 Estimated Loss: {result['estimated_loss']}")
    print(f"🦠 Disease Alert: {result['disease_alert']}")
    print(f"\n🌾 Crop Category: {result['crop_category']}")
    print(f"📅 Best Season: {result['season']}")
    print(f"💧 Water Need: {result['water_need']}")
    print(f"🧪 Nutrient Need: {result['nutrient_need']}")
    print(f"🌱 Expected Yield: {result['expected_yield']}")
    
    print(f"\n⚙️ Optimal Parameters:")
    for key, value in result['optimal_parameters'].items():
        print(f"   {key}: {value}")
    
    print(f"\n🏥 Common Diseases: {', '.join(result['common_diseases'])}")
    print(f"\n📍 Suitable Regions: {', '.join(result['suitable_regions'])}")
    
    print(f"\n💡 Recommendations:")
    for rec in result['recommendations']:
        print(f"   • {rec}")
    
    print(f"\n📝 Action Plan:\n{result['action_plan']}")
