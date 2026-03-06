"""
AgriGuard AI Database Population Script
Populates the SQLite database with comprehensive agricultural data
"""

import sqlite3
import os

# Get the database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'agriguard.db')

def create_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def populate_seasons(conn):
    """Populate seasons table"""
    seasons = [
        ("Kharif", "June,July,August,September", 1, 1, "Monsoon season - for rice main planting season and other crops"),
        ("Rabi", "October,November,December,January,February,March", 0, 0, "Winter season - wheat and other winter crops"),
        ("Zaid", "April,May", 0, 0, "Summer season - short duration crops")
    ]
    
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR IGNORE INTO seasons (season_name, months, monsoon_active, rain_likely, description) VALUES (?, ?, ?, ?, ?)",
        seasons
    )
    conn.commit()
    print("✓ Seasons populated")

def populate_regions(conn):
    """Populate regions table"""
    regions = [
        ("Punjab", "Semi-arid", 650, "Granary of India - major wheat and rice producer"),
        ("West Bengal", "Humid Subtropical", 1500, "Rice bowl of India - diverse crops"),
        ("Tamil Nadu", "Tropical Savanna", 900, "Diversified agriculture - rice, cotton, sugarcane"),
        ("Andhra Pradesh", "Semi-arid to Tropical", 900, "Rice, cotton, maize, pulses production"),
        ("Karnataka", "Semi-arid", 1100, "Diverse climate - cereals, pulses, oilseeds"),
        ("Maharashtra", "Tropical Savanna", 1100, "Major producer of sugarcane, cotton, jowar"),
        ("Madhya Pradesh", "Semi-arid", 1200, "Soybean, wheat, pulses production"),
        ("Rajasthan", "Arid to Semi-arid", 300, "Bajra, wheat, mustard - irrigation dependent"),
        ("Uttar Pradesh", "Humid Subtropical", 1000, "Most populous state - diverse crops"),
        ("Gujarat", "Semi-arid", 800, "Cotton, groundnut, wheat production"),
        ("Haryana", "Semi-arid", 600, "Wheat, rice, cotton - green revolution state"),
        ("Bihar", "Humid Subtropical", 1200, "Rice, wheat, maize production"),
        ("Odisha", "Humid Subtropical", 1500, "Rice, pulses, oilseeds production"),
        ("Kerala", "Humid Tropical", 2800, "Rice, coconut, pepper, rubber"),
        ("Telangana", "Semi-arid", 900, "Rice, cotton, maize, pulses")
    ]
    
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR IGNORE INTO regions (region_name, climate_type, avg_rainfall_mm, description) VALUES (?, ?, ?, ?)",
        regions
    )
    conn.commit()
    print("✓ Regions populated")

def populate_crops(conn):
    """Populate crops table with comprehensive data"""
    
    # First get season IDs
    cursor = conn.cursor()
    cursor.execute("SELECT season_id, season_name FROM seasons")
    seasons = dict(cursor.fetchall())
    
    crops = [
        # CEREALS
        ("Rice", "Cereal", "Kharif", "High", "High N", "Jun-Jul", "Nov-Dec", 3, 6, "tonnes/acre", "Staple food crop - primary source of calories for billions"),
        ("Wheat", "Cereal", "Rabi", "Medium", "High NPK", "Oct-Nov", "Mar-Apr", 2.5, 4.5, "tonnes/acre", "Second most important cereal crop - staple for billions"),
        ("Maize", "Cereal", "Kharif/Rabi", "Medium-High", "High NPK", "Jun-Jul", "Oct-Nov", 2.5, 5, "tonnes/acre", "Versatile crop - food, feed, and industrial uses"),
        ("Bajra", "Cereal", "Kharif", "Low", "Medium", "Jul-Aug", "Oct-Nov", 1.5, 2.5, "tonnes/acre", "Drought resistant - food for marginal farmers"),
        ("Jowar", "Cereal", "Kharif/Rabi", "Low-Medium", "Medium", "Jun-Jul", "Sep-Nov", 1.5, 3, "tonnes/area", "Drought tolerant - important fodder crop"),
        ("Ragi", "Cereal", "Kharif", "Low-Medium", "Low-Medium", "Jun-Jul", "Nov-Dec", 1.5, 2.5, "tonnes/acre", "Nutritious millet - rich in calcium and iron"),
        
        # PULSES
        ("Gram", "Pulse", "Rabi", "Low-Medium", "Low (N-fixing)", "Oct-Nov", "Feb-Mar", 1, 2, "tonnes/acre", "Most important pulse - protein-rich"),
        ("Tur", "Pulse", "Kharif", "Medium", "Low (N-fixing)", "Jun-Jul", "Nov-Feb", 1.5, 2.5, "tonnes/acre", "Major protein source - pigeon pea"),
        ("Moong", "Pulse", "Kharif/Rabi", "Low-Medium", "Low", "Jun-Jul/Sep-Oct", "Sep-Oct/Dec-Jan", 0.8, 1.5, "tonnes/acre", "Quick growing - green gram"),
        ("Urhad", "Pulse", "Kharif", "Medium", "Low (N-fixing)", "Jun-Jul", "Oct-Nov", 0.8, 1.5, "tonnes/acre", "Black gram - protein rich"),
        ("Peas", "Pulse", "Rabi", "Medium", "Medium", "Oct-Nov", "Feb-Mar", 1, 2, "tonnes/acre", "Vegetable and grain - high protein"),
        ("Lentil", "Pulse", "Rabi", "Low-Medium", "Low", "Oct-Nov", "Feb-Mar", 0.8, 1.5, "tonnes/acre", "Rich in protein and iron"),
        
        # OILSEEDS
        ("Groundnut", "Oilseed", "Kharif/Rabi", "Medium", "Medium-High", "Jun-Jul/Oct-Nov", "Oct-Nov/Feb-Mar", 1.5, 2.5, "tonnes/acre", "Major oilseed - rich in protein"),
        ("Mustard", "Oilseed", "Rabi", "Low-Medium", "Medium", "Oct-Nov", "Feb-Mar", 1, 1.8, "tonnes/acre", "Important rabi oilseed - edible oil"),
        ("Soybean", "Oilseed", "Kharif", "Medium", "Medium-High", "Jun-Jul", "Sep-Oct", 1.5, 2.5, "tonnes/acre", "High protein - industrial and food uses"),
        ("Sunflower", "Oilseed", "Kharif/Rabi", "Medium", "Medium-High", "Jun-Jul/Oct-Nov", "Sep-Oct/Jan-Feb", 1, 1.8, "tonnes/acre", "Premium oilseed - high yielding"),
        ("Sesame", "Oilseed", "Kharif", "Low-Medium", "Low", "Jun-Jul", "Sep-Oct", 0.3, 0.5, "tonnes/acre", "High oil content - export commodity"),
        ("Linseed", "Oilseed", "Rabi", "Low-Medium", "Medium", "Oct-Nov", "Feb-Mar", 0.5, 0.8, "tonnes/acre", "Industrial and edible oil"),
        
        # CASH CROPS
        ("Sugarcane", "Cash Crop", "Annual", "Very High", "Very High NPK", "Feb-Mar/Oct-Nov", "12-18 months", 40, 70, "tonnes/acre", "Major sweetener - jaggery and sugar"),
        ("Cotton", "Cash Crop", "Kharif", "Medium-High", "High NPK", "May-Jun", "Sep-Dec", 1.5, 3, "quintals/acre", "White gold - textile industry"),
        ("Jute", "Cash Crop", "Kharif", "High", "Medium", "Mar-May", "Jul-Oct", 1.5, 2.5, "tonnes/acre", "B多元化纤维 - packaging industry"),
        ("Tobacco", "Cash Crop", "Rabi/Kharif", "Medium", "High", "Oct-Nov/Jun-Jul", "Feb-Apr", 1.5, 2.5, "tonnes/acre", "Commercial crop - export commodity"),
        
        # VEGETABLES
        ("Tomato", "Vegetable", "Rabi/Kharif", "Medium-High", "High NPK", "Jun-Jul/Oct-Nov", "90-120 days", 10, 20, "tonnes/acre", "Most consumed vegetable - rich in lycopene"),
        ("Potato", "Vegetable", "Rabi", "Medium", "High NPK", "Oct-Nov", "90-120 days", 8, 15, "tonnes/acre", "Fourth most important food crop"),
        ("Onion", "Vegetable", "Rabi/Kharif", "Medium", "Medium-High", "Sep-Nov/May-Jun", "90-150 days", 8, 15, "tonnes/acre", "Essential culinary ingredient"),
        ("Cabbage", "Vegetable", "Rabi", "Medium-High", "High N", "Sep-Nov", "70-120 days", 20, 40, "tonnes/acre", "Cool season crop - rich in vitamins"),
        ("Cauliflower", "Vegetable", "Rabi", "Medium-High", "High N", "Sep-Nov", "65-90 days", 15, 30, "tonnes/acre", "Cool season crop - nutritious"),
        ("Carrot", "Vegetable", "Rabi", "Medium", "Medium", "Sep-Nov", "90-120 days", 8, 15, "tonnes/acre", "Rich in beta-carotene"),
        ("Brinjal", "Vegetable", "Kharif/Rabi", "Medium-High", "Medium-High", "Jun-Jul/Oct-Nov", "90-120 days", 15, 25, "tonnes/acre", "Eggplant - popular vegetable"),
        ("Okra", "Vegetable", "Kharif", "Medium-High", "Medium", "Jun-Jul", "45-60 days", 6, 12, "tonnes/acre", "Lady's finger - rich in fiber"),
        ("Spinach", "Vegetable", "Rabi", "Medium", "High N", "Sep-Nov", "45-60 days", 5, 10, "tonnes/acre", "Leafy green - rich in iron"),
        ("Chilli", "Vegetable", "Kharif/Rabi", "Medium", "High NPK", "Jun-Jul/Oct-Nov", "60-90 days", 2, 4, "tonnes/acre", "Spice crop - high value"),
        
        # FRUITS
        ("Mango", "Fruit", "Summer", "Medium", "Medium-High", "Jan-Feb (flowering)", "Apr-Jul", 5, 15, "tonnes/acre", "King of fruits - export quality"),
        ("Banana", "Fruit", "Year-round", "Very High", "Very High", "Mar-May/Sep-Nov", "9-12 months", 20, 40, "tonnes/acre", "Most consumed fruit globally"),
        ("Papaya", "Fruit", "Year-round", "Medium-High", "Medium-High", "Feb-Apr/Aug-Oct", "8-12 months", 30, 60, "tonnes/acre", "Quick growing - medicinal properties"),
        ("Guava", "Fruit", "Winter", "Medium", "Medium", "Jun-Sep (flowering)", "Nov-Mar", 8, 20, "tonnes/acre", "Vitamin C rich - popular fruit"),
        ("Pomegranate", "Fruit", "Winter", "Low-Medium", "Medium", "Mar-May", "Sep-Dec", 8, 15, "tonnes/acre", "High antioxidant - medicinal"),
        ("Grapes", "Fruit", "Summer", "Medium-High", "High", "Apr-May/Oct-Nov", "Jun-Sep/Dec-Mar", 8, 15, "tonnes/acre", "Wine production - table fruit"),
        ("Citrus", "Fruit", "Winter", "Medium", "Medium", "Jun-Aug", "Nov-Mar", 10, 20, "tonnes/acre", "Oranges, lemons - vitamin C"),
        ("Apple", "Fruit", "Winter", "Medium", "High", "Jan-Feb", "Aug-Oct", 10, 20, "tonnes/acre", "Temperate fruit - high value"),
        ("Litchi", "Fruit", "Summer", "Medium", "Medium", "Jan-Feb", "May-Jul", 5, 10, "tonnes/acre", "Premium fruit - export quality"),
        ("Pineapple", "Fruit", "Year-round", "Medium-High", "Medium-High", "Jan-Mar/Apr-Jun", "18-24 months", 20, 40, "tonnes/acre", "Tropical fruit - processing industry"),
    ]
    
    cursor.executemany(
        """INSERT OR IGNORE INTO crops 
           (crop_name, category, season_id, water_need, nutrient_need, sowing_period, harvest_period, yield_min, yield_max, yield_unit, description) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        [(c[0], c[1], seasons.get(c[2]), *c[3:]) for c in crops]
    )
    conn.commit()
    print("✓ Crops populated")

def populate_crop_parameters(conn):
    """Populate crop parameters table"""
    cursor = conn.cursor()
    
    # Get all crops
    cursor.execute("SELECT crop_id, crop_name FROM crops")
    crops = dict(cursor.fetchall())
    
    parameters = []
    
    # Rice
    if "Rice" in crops:
        rice_id = crops["Rice"]
        parameters.extend([
            (rice_id, "optimal", 150, 250, 20, 30, 70, 90, 5.5, 7.0),
            (rice_id, "tolerance", 100, 300, 15, 35, 60, 95, 5.0, 8.0),
        ])
    
    # Wheat
    if "Wheat" in crops:
        wheat_id = crops["Wheat"]
        parameters.extend([
            (wheat_id, "optimal", 50, 120, 15, 25, 40, 70, 6.0, 7.5),
            (wheat_id, "tolerance", 25, 150, 10, 30, 30, 80, 5.5, 8.0),
        ])
    
    # Maize
    if "Maize" in crops:
        maize_id = crops["Maize"]
        parameters.extend([
            (maize_id, "optimal", 60, 150, 22, 32, 50, 80, 5.8, 7.0),
            (maize_id, "tolerance", 40, 200, 18, 35, 40, 90, 5.5, 7.5),
        ])
    
    # Bajra
    if "Bajra" in crops:
        bajra_id = crops["Bajra"]
        parameters.extend([
            (bajra_id, "optimal", 40, 80, 25, 35, 30, 60, 6.5, 8.0),
            (bajra_id, "tolerance", 20, 120, 20, 40, 20, 80, 5.5, 8.5),
        ])
    
    # Jowar
    if "Jowar" in crops:
        jowar_id = crops["Jowar"]
        parameters.extend([
            (jowar_id, "optimal", 45, 100, 25, 35, 35, 70, 6.0, 7.5),
            (jowar_id, "tolerance", 30, 150, 20, 40, 25, 85, 5.5, 8.0),
        ])
    
    # Ragi
    if "Ragi" in crops:
        ragi_id = crops["Ragi"]
        parameters.extend([
            (ragi_id, "optimal", 50, 120, 20, 30, 50, 80, 5.5, 7.0),
            (ragi_id, "tolerance", 30, 150, 15, 35, 40, 90, 5.0, 7.5),
        ])
    
    # Gram
    if "Gram" in crops:
        gram_id = crops["Gram"]
        parameters.extend([
            (gram_id, "optimal", 40, 80, 20, 30, 35, 60, 6.0, 7.5),
            (gram_id, "tolerance", 25, 100, 15, 35, 25, 75, 5.5, 8.0),
        ])
    
    # Tur
    if "Tur" in crops:
        tur_id = crops["Tur"]
        parameters.extend([
            (tur_id, "optimal", 60, 120, 22, 32, 50, 70, 5.5, 7.0),
            (tur_id, "tolerance", 40, 180, 18, 38, 35, 85, 5.0, 7.5),
        ])
    
    # Moong
    if "Moong" in crops:
        moong_id = crops["Moong"]
        parameters.extend([
            (moong_id, "optimal", 50, 100, 25, 35, 40, 70, 6.0, 7.5),
            (moong_id, "tolerance", 30, 150, 20, 40, 30, 85, 5.5, 8.0),
        ])
    
    # Groundnut
    if "Groundnut" in crops:
        groundnut_id = crops["Groundnut"]
        parameters.extend([
            (groundnut_id, "optimal", 50, 120, 24, 32, 40, 70, 5.5, 7.0),
            (groundnut_id, "tolerance", 30, 180, 20, 38, 30, 85, 5.0, 7.5),
        ])
    
    # Mustard
    if "Mustard" in crops:
        mustard_id = crops["Mustard"]
        parameters.extend([
            (mustard_id, "optimal", 40, 80, 15, 25, 35, 65, 6.0, 7.5),
            (mustard_id, "tolerance", 20, 120, 10, 32, 25, 80, 5.5, 8.0),
        ])
    
    # Soybean
    if "Soybean" in crops:
        soybean_id = crops["Soybean"]
        parameters.extend([
            (soybean_id, "optimal", 60, 120, 20, 32, 50, 70, 6.0, 7.0),
            (soybean_id, "tolerance", 40, 180, 15, 38, 35, 85, 5.5, 7.5),
        ])
    
    # Sunflower
    if "Sunflower" in crops:
        sunflower_id = crops["Sunflower"]
        parameters.extend([
            (sunflower_id, "optimal", 50, 100, 20, 30, 45, 70, 6.0, 7.5),
            (sunflower_id, "tolerance", 30, 150, 15, 35, 35, 85, 5.5, 8.0),
        ])
    
    # Sugarcane
    if "Sugarcane" in crops:
        sugarcane_id = crops["Sugarcane"]
        parameters.extend([
            (sugarcane_id, "optimal", 200, 300, 24, 34, 70, 85, 6.5, 7.5),
            (sugarcane_id, "tolerance", 150, 400, 18, 40, 50, 95, 6.0, 8.0),
        ])
    
    # Cotton
    if "Cotton" in crops:
        cotton_id = crops["Cotton"]
        parameters.extend([
            (cotton_id, "optimal", 60, 120, 25, 35, 50, 70, 6.0, 7.5),
            (cotton_id, "tolerance", 40, 180, 18, 42, 35, 85, 5.5, 8.0),
        ])
    
    # Tomato
    if "Tomato" in crops:
        tomato_id = crops["Tomato"]
        parameters.extend([
            (tomato_id, "optimal", 60, 120, 20, 28, 60, 80, 6.0, 7.0),
            (tomato_id, "tolerance", 40, 180, 15, 35, 50, 90, 5.5, 7.5),
        ])
    
    # Potato
    if "Potato" in crops:
        potato_id = crops["Potato"]
        parameters.extend([
            (potato_id, "optimal", 50, 100, 15, 25, 60, 80, 5.5, 6.5),
            (potato_id, "tolerance", 30, 150, 10, 30, 50, 90, 5.0, 7.0),
        ])
    
    # Onion
    if "Onion" in crops:
        onion_id = crops["Onion"]
        parameters.extend([
            (onion_id, "optimal", 50, 100, 20, 30, 50, 70, 6.0, 7.5),
            (onion_id, "tolerance", 30, 150, 15, 35, 40, 85, 5.5, 8.0),
        ])
    
    # Cabbage
    if "Cabbage" in crops:
        cabbage_id = crops["Cabbage"]
        parameters.extend([
            (cabbage_id, "optimal", 50, 100, 15, 22, 70, 85, 6.0, 7.0),
            (cabbage_id, "tolerance", 30, 150, 10, 28, 60, 95, 5.5, 7.5),
        ])
    
    # Cauliflower
    if "Cauliflower" in crops:
        cauliflower_id = crops["Cauliflower"]
        parameters.extend([
            (cauliflower_id, "optimal", 50, 100, 15, 22, 70, 85, 6.0, 7.0),
            (cauliflower_id, "tolerance", 30, 150, 10, 28, 60, 95, 5.5, 7.5),
        ])
    
    # Carrot
    if "Carrot" in crops:
        carrot_id = crops["Carrot"]
        parameters.extend([
            (carrot_id, "optimal", 40, 80, 18, 26, 60, 75, 6.0, 7.0),
            (carrot_id, "tolerance", 25, 120, 10, 32, 50, 85, 5.5, 7.5),
        ])
    
    # Brinjal
    if "Brinjal" in crops:
        brinjal_id = crops["Brinjal"]
        parameters.extend([
            (brinjal_id, "optimal", 60, 120, 24, 32, 60, 75, 6.0, 7.0),
            (brinjal_id, "tolerance", 40, 180, 18, 38, 50, 85, 5.5, 7.5),
        ])
    
    # Okra
    if "Okra" in crops:
        okra_id = crops["Okra"]
        parameters.extend([
            (okra_id, "optimal", 60, 120, 25, 35, 60, 80, 6.0, 7.0),
            (okra_id, "tolerance", 40, 180, 20, 40, 50, 90, 5.5, 7.5),
        ])
    
    # Mango
    if "Mango" in crops:
        mango_id = crops["Mango"]
        parameters.extend([
            (mango_id, "optimal", 100, 200, 24, 32, 50, 70, 6.0, 7.0),
            (mango_id, "tolerance", 50, 300, 18, 42, 35, 85, 5.5, 7.5),
        ])
    
    # Banana
    if "Banana" in crops:
        banana_id = crops["Banana"]
        parameters.extend([
            (banana_id, "optimal", 150, 250, 26, 32, 70, 85, 6.0, 7.0),
            (banana_id, "tolerance", 100, 400, 18, 38, 50, 95, 5.5, 7.5),
        ])
    
    # Papaya
    if "Papaya" in crops:
        papaya_id = crops["Papaya"]
        parameters.extend([
            (papaya_id, "optimal", 100, 200, 24, 32, 60, 75, 6.0, 7.0),
            (papaya_id, "tolerance", 50, 300, 18, 38, 45, 90, 5.5, 7.5),
        ])
    
    # Guava
    if "Guava" in crops:
        guava_id = crops["Guava"]
        parameters.extend([
            (guava_id, "optimal", 100, 180, 23, 32, 50, 70, 6.5, 7.5),
            (guava_id, "tolerance", 50, 250, 18, 38, 40, 85, 5.5, 8.0),
        ])
    
    # Pomegranate
    if "Pomegranate" in crops:
        pomegranate_id = crops["Pomegranate"]
        parameters.extend([
            (pomegranate_id, "optimal", 50, 120, 25, 35, 40, 60, 6.5, 7.5),
            (pomegranate_id, "tolerance", 30, 200, 18, 42, 30, 80, 5.5, 8.0),
        ])
    
    # Grapes
    if "Grapes" in crops:
        grapes_id = crops["Grapes"]
        parameters.extend([
            (grapes_id, "optimal", 50, 100, 24, 32, 50, 70, 6.5, 7.5),
            (grapes_id, "tolerance", 30, 150, 18, 38, 40, 85, 6.0, 8.0),
        ])
    
    cursor.executemany(
        """INSERT OR IGNORE INTO crop_parameters 
           (crop_id, param_type, rainfall_min_mm, rainfall_max_mm, temp_min_c, temp_max_c, humidity_min, humidity_max, ph_min, ph_max) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        parameters
    )
    conn.commit()
    print("✓ Crop parameters populated")

def populate_diseases(conn):
    """Populate diseases table"""
    diseases = [
        ("Blast", "Fungal", "High", 
         "Diamond-shaped lesions with gray centers on leaves, neck rot causing empty panicles",
         "Temperature 20-30°C, Humidity 80-100%, High rainfall",
         "Tricyclazole 75% WP @ 0.6 g/L or Isoprothiolane",
         "Neem oil 5ml/L, remove infected leaves",
         "Use resistant varieties, avoid excessive N fertilizer, maintain proper spacing"),
        
        ("Bacterial Leaf Blight", "Bacterial", "High",
         "Yellow to white lesions starting from leaf tips, bacterial ooze visible in morning",
         "Temperature 25-34°C, Humidity 80-100%, High rainfall",
         "Copper Oxychloride 50% WP @ 2.5 g/L",
         "Neem extract, biocontrol agents",
         "Use certified seeds, avoid working in wet fields, crop rotation"),
        
        ("Brown Spot", "Fungal", "Moderate",
         "Brown oval spots on leaves, can cause grain discoloration",
         "Temperature 25-32°C, Humidity 70-90%, Moderate rainfall",
         "Mancozeb 75% WP @ 2.5 g/L",
         "Neem extract, garlic extract",
         "Use healthy seeds, adequate fertilization, remove crop residues"),
        
        ("Sheath Blight", "Fungal", "High",
         "Lesions on leaf sheath, white fungal growth, lodging of plants",
         "Temperature 28-32°C, Humidity 85-100%, High humidity",
         "Validamycin 3% L @ 2 ml/L or Hexaconazole",
         "Trichoderma viride, neem cake",
         "Use resistant varieties, avoid dense planting, balanced N fertilization"),
        
        ("Rust", "Fungal", "High",
         "Orange-brown pustules on leaves and stems, causes premature drying",
         "Temperature 15-25°C, Humidity 70-90%, Moderate rainfall",
         "Propiconazole 25% EC @ 1 ml/L or Mancozeb",
         "Baking soda spray, sulfur dust",
         "Use resistant varieties, early sowing, remove crop residues"),
        
        ("Powdery Mildew", "Fungal", "Moderate",
         "White powdery coating on leaves, stems, and fruits, yellowing of leaves",
         "Temperature 20-30°C, Humidity 50-70%, Low rainfall",
         "Sulfur 80% WDG @ 2 g/L or Carbendazim",
         "Neem oil, milk spray (1:9 ratio)",
         "Adequate spacing, avoid excess nitrogen, resistant varieties"),
        
        ("Karnal Bunt", "Fungal", "High",
         "Partial or complete grain conversion to black powder, fishy odor",
         "Temperature 15-25°C, Humidity 70-80%, Cool and moist conditions",
         "Carbendazim 50% WP or Propiconazole",
         "Solar treatment of seeds, biocontrol agents",
         "Use certified seeds, avoid late sowing, crop rotation"),
        
        ("Leaf Blight", "Fungal", "Moderate",
         "Brown to necrotic lesions on leaves, can cause leaf drying",
         "Temperature 20-30°C, Humidity 70-90%, Moderate-High rainfall",
         "Mancozeb 75% WP @ 2.5 g/L or Chlorothalonil",
         "Neem extract, garlic extract",
         "Remove infected debris, adequate spacing, avoid overhead irrigation"),
        
        ("Downy Mildew", "Fungal", "Moderate",
         "Yellowish spots on upper leaf surface, white mold on undersides",
         "Temperature 15-25°C, Humidity 80-100%, Cool and humid",
         "Metalaxyl + Mancozeb or Ridomil",
         "Bordeaux mixture, neem oil",
         "Use resistant varieties, proper spacing, avoid overhead irrigation"),
        
        ("Wilt", "Fungal/Bacterial", "High",
         "Wilting despite adequate water, yellowing, vascular discoloration",
         "Temperature 25-35°C, Humidity 60-80%, Moderate rainfall",
         "Carbendazim 50% WP or Trichoderma viride",
         "Neem cake, biocontrol",
         "Use resistant varieties, crop rotation, solarization, avoid waterlogging"),
        
        ("Yellow Mosaic Virus", "Viral", "High",
         "Yellow mottling and mosaic patterns on leaves, stunted growth",
         "Temperature 25-35°C, Humidity 60-80%, Moderate rainfall",
         "No direct treatment - control vectors",
         "Neem oil to repel vectors",
         "Use resistant varieties, control whiteflies/jassids, early sowing"),
        
        ("Late Blight", "Fungal", "Very High",
         "Water-soaked lesions turning brown, white mold on leaf undersides",
         "Temperature 15-22°C, Humidity 90-100%, High rainfall",
         "Metalaxyl + Mancozeb or Mancozeb alone",
         "Bordeaux mixture, remove infected plants",
         "Use resistant varieties, avoid overhead irrigation, proper spacing"),
        
        ("Early Blight", "Fungal", "Moderate",
         "Dark brown spots with concentric rings (target spot pattern)",
         "Temperature 24-29°C, Humidity 70-90%, Moderate rainfall",
         "Mancozeb 75% WP or Chlorothalonil",
         "Neem oil, compost tea",
         "Crop rotation, remove infected debris, mulching"),
        
        ("Bacterial Wilt", "Bacterial", "High",
         "Wilting, yellowing, brown vascular tissue when stem is cut",
         "Temperature 25-35°C, Humidity 60-80%, Moderate rainfall",
         "Streptocycline + Copper Oxychloride",
         "Biocontrol agents, crop rotation",
         "Use resistant varieties, avoid infected fields, proper drainage"),
        
        ("Tomato Leaf Curl", "Viral", "High",
         "Leaf curling, thickening of veins, stunted growth",
         "Temperature 25-35°C, Humidity 50-70%, Dry conditions",
         "No direct treatment - control whiteflies",
         "Neem oil, yellow sticky traps",
         "Use resistant varieties, control whiteflies, early planting"),
        
        ("Red Rot", "Fungal", "High",
         "Red stripes on leaves, internal pith shows red with white spots",
         "Temperature 25-35°C, Humidity 70-90%, Moderate rainfall",
         "Carbendazim or Thiophanate methyl",
         "Heat treatment of seed sets",
         "Use healthy seed, crop rotation, resistant varieties"),
        
        ("Cotton Wilt", "Fungal", "High",
         "Wilting, yellowing starting from lower leaves, brown vascular tissue",
         "Temperature 28-38°C, Humidity 60-80%, Moderate rainfall",
         "Carbendazim or Trichoderma",
         "Neem cake, biofertilizers",
         "Use resistant varieties, crop rotation with legumes, avoid monoculture"),
        
        ("Cotton Leaf Curl Virus", "Viral", "High",
         "Leaf curling, thickening, enations on leaf undersides",
         "Temperature 28-38°C, Humidity 60-80%, Moderate rainfall",
         "No direct treatment - control whiteflies",
         "Neem oil, insect traps",
         "Use resistant varieties, early sowing, control vectors"),
        
        ("Boll Rot", "Fungal", "Moderate",
         "Brown water-soaked lesions on bolls, boll shedding",
         "Temperature 25-35°C, Humidity 70-90%, High humidity",
         "Mancozeb or Carbendazim",
         "Neem oil, proper plant spacing",
         "Avoid excessive irrigation, control boll weevil, proper drainage"),
        
        ("Mango Hopper", "Insect", "High",
         "Hoppers on buds/leaves, honeydew sooty mold, flower dropping",
         "Temperature 25-35°C, Humidity 60-80%, Moderate rainfall",
         "Imidacloprid 17.8% SL or Cyantraniliprole",
         "Neem oil, yellow sticky traps",
         "Monitoring, early morning spray, destroy fallen fruits"),
        
        ("Fruit Fly", "Insect", "High",
         "Fruit damage, maggots inside fruits, rotting",
         "Temperature 25-35°C, Humidity 60-80%, Low-Moderate rainfall",
         "Malathion 50% EC + sugar, protein hydrolysate",
         "Cuelure traps, bagging fruits",
         "Orchard sanitation, early harvesting, male annihilation technique"),
        
        ("Stem Borer", "Insect", "High",
         "Dead hearts in young plants, bore holes in stems, white heads",
         "Temperature 25-35°C, Humidity 60-80%, Moderate rainfall",
         "Carbofuran or Fipronil",
         "Neem oil, biological control",
         "Use resistant varieties, destroy crop residues, timely harvest"),
        
        ("Aphids", "Insect", "Moderate",
         "Curling leaves, honeydew sooty mold, stunted growth",
         "Temperature 20-30°C, Humidity 40-70%, Moderate",
         "Imidacloprid or Thiamethoxam",
         "Neem oil, soap solution, ladybirds",
         "Use resistant varieties, avoid excess nitrogen, biological control"),
        
        ("Pink Bollworm", "Insect", "High",
         "Bore into bolls, damaged lint, reduced yield",
         "Temperature 25-35°C, Humidity 50-70%, Dry",
         "Spinosad or Indoxacarb",
         "Pheromone traps, neem oil",
         "Early harvest, crop rotation, BT cotton"),
        
        ("Anthracnose", "Fungal", "Moderate",
         "Dark sunken lesions on fruits, leaves, and stems",
         "Temperature 20-30°C, Humidity 80-90%, High humidity",
         "Carbendazim or Mancozeb",
         "Neem oil, copper-based fungicides",
         "Use resistant varieties, proper pruning, orchard sanitation"),
        
        ("Panama Wilt", "Fungal", "Very High",
         "Yellowing of lower leaves, vascular discoloration, plant death",
         "Temperature 25-30°C, Humidity 70-90%, High moisture",
         "No effective chemical control",
         "Soil solarization, biocontrol",
         "Use resistant varieties, avoid infected soil, crop rotation"),
        
        ("Sigatoka Leaf Spot", "Fungal", "High",
         "Brown streaks on leaves, premature leaf death",
         "Temperature 25-30°C, Humidity 80-95%, High rainfall",
         "Mancozeb or Propiconazole",
         "Neem oil, proper drainage",
         "Use resistant varieties, remove infected leaves, proper spacing"),
    ]
    
    cursor = conn.cursor()
    cursor.executemany(
        """INSERT OR IGNORE INTO diseases 
           (disease_name, disease_type, severity, symptoms, conditions_favoured, treatment_chemical, treatment_organic, prevention) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        diseases
    )
    conn.commit()
    print("✓ Diseases populated")

def populate_crop_diseases(conn):
    """Populate crop-diseases junction table"""
    cursor = conn.cursor()
    
    # Get crop and disease IDs
    cursor.execute("SELECT crop_id, crop_name FROM crops")
    crops = dict(cursor.fetchall())
    
    cursor.execute("SELECT disease_id, disease_name FROM diseases")
    diseases = dict(cursor.fetchall())
    
    crop_disease_links = []
    
    # Rice diseases
    if "Rice" in crops and "Blast" in diseases:
        crop_disease_links.append((crops["Rice"], diseases["Blast"]))
    if "Rice" in crops and "Bacterial Leaf Blight" in diseases:
        crop_disease_links.append((crops["Rice"], diseases["Bacterial Leaf Blight"]))
    if "Rice" in crops and "Brown Spot" in diseases:
        crop_disease_links.append((crops["Rice"], diseases["Brown Spot"]))
    if "Rice" in crops and "Sheath Blight" in diseases:
        crop_disease_links.append((crops["Rice"], diseases["Sheath Blight"]))
    
    # Wheat diseases
    if "Wheat" in crops and "Rust" in diseases:
        crop_disease_links.append((crops["Wheat"], diseases["Rust"]))
    if "Wheat" in crops and "Powdery Mildew" in diseases:
        crop_disease_links.append((crops["Wheat"], diseases["Powdery Mildew"]))
    if "Wheat" in crops and "Karnal Bunt" in diseases:
        crop_disease_links.append((crops["Wheat"], diseases["Karnal Bunt"]))
    if "Wheat" in crops and "Leaf Blight" in diseases:
        crop_disease_links.append((crops["Wheat"], diseases["Leaf Blight"]))
    
    # Maize diseases
    if "Maize" in crops and "Leaf Blight" in diseases:
        crop_disease_links.append((crops["Maize"], diseases["Leaf Blight"]))
    if "Maize" in crops and "Rust" in diseases:
        crop_disease_links.append((crops["Maize"], diseases["Rust"]))
    if "Maize" in crops and "Downy Mildew" in diseases:
        crop_disease_links.append((crops["Maize"], diseases["Downy Mildew"]))
    
    # Bajra diseases
    if "Bajra" in crops and "Downy Mildew" in diseases:
        crop_disease_links.append((crops["Bajra"], diseases["Downy Mildew"]))
    if "Bajra" in crops and "Rust" in diseases:
        crop_disease_links.append((crops["Bajra"], diseases["Rust"]))
    if "Bajra" in crops and "Leaf Blight" in diseases:
        crop_disease_links.append((crops["Bajra"], diseases["Leaf Blight"]))
    
    # Gram diseases
    if "Gram" in crops and "Wilt" in diseases:
        crop_disease_links.append((crops["Gram"], diseases["Wilt"]))
    if "Gram" in crops and "Powdery Mildew" in diseases:
        crop_disease_links.append((crops["Gram"], diseases["Powdery Mildew"]))
    if "Gram" in crops and "Rust" in diseases:
        crop_disease_links.append((crops["Gram"], diseases["Rust"]))
    
    # Tur diseases
    if "Tur" in crops and "Powdery Mildew" in diseases:
        crop_disease_links.append((crops["Tur"], diseases["Powdery Mildew"]))
    if "Tur" in crops and "Wilt" in diseases:
        crop_disease_links.append((crops["Tur"], diseases["Wilt"]))
    if "Tur" in crops and "Yellow Mosaic Virus" in diseases:
        crop_disease_links.append((crops["Tur"], diseases["Yellow Mosaic Virus"]))
    
    # Moong diseases
    if "Moong" in crops and "Yellow Mosaic Virus" in diseases:
        crop_disease_links.append((crops["Moong"], diseases["Yellow Mosaic Virus"]))
    if "Moong" in crops and "Powdery Mildew" in diseases:
        crop_disease_links.append((crops["Moong"], diseases["Powdery Mildew"]))
    
    # Groundnut diseases
    if "Groundnut" in crops and "Leaf Blight" in diseases:
        crop_disease_links.append((crops["Groundnut"], diseases["Leaf Blight"]))
    if "Groundnut" in crops and "Rust" in diseases:
        crop_disease_links.append((crops["Groundnut"], diseases["Rust"]))
    
    # Mustard diseases
    if "Mustard" in crops and "White Rust" in diseases:
        crop_disease_links.append((crops["Mustard"], diseases["White Rust"]))
    if "Mustard" in crops and "Powdery Mildew" in diseases:
        crop_disease_links.append((crops["Mustard"], diseases["Powdery Mildew"]))
    
    # Soybean diseases
    if "Soybean" in crops and "Yellow Mosaic Virus" in diseases:
        crop_disease_links.append((crops["Soybean"], diseases["Yellow Mosaic Virus"]))
    if "Soybean" in crops and "Rust" in diseases:
        crop_disease_links.append((crops["Soybean"], diseases["Rust"]))
    
    # Sugarcane diseases
    if "Sugarcane" in crops and "Red Rot" in diseases:
        crop_disease_links.append((crops["Sugarcane"], diseases["Red Rot"]))
    
    # Cotton diseases
    if "Cotton" in crops and "Cotton Wilt" in diseases:
        crop_disease_links.append((crops["Cotton"], diseases["Cotton Wilt"]))
    if "Cotton" in crops and "Cotton Leaf Curl Virus" in diseases:
        crop_disease_links.append((crops["Cotton"], diseases["Cotton Leaf Curl Virus"]))
    if "Cotton" in crops and "Boll Rot" in diseases:
        crop_disease_links.append((crops["Cotton"], diseases["Boll Rot"]))
    
    # Tomato diseases
    if "Tomato" in crops and "Late Blight" in diseases:
        crop_disease_links.append((crops["Tomato"], diseases["Late Blight"]))
    if "Tomato" in crops and "Early Blight" in diseases:
        crop_disease_links.append((crops["Tomato"], diseases["Early Blight"]))
    if "Tomato" in crops and "Bacterial Wilt" in diseases:
        crop_disease_links.append((crops["Tomato"], diseases["Bacterial Wilt"]))
    if "Tomato" in crops and "Tomato Leaf Curl" in diseases:
        crop_disease_links.append((crops["Tomato"], diseases["Tomato Leaf Curl"]))
    
    # Potato diseases
    if "Potato" in crops and "Late Blight" in diseases:
        crop_disease_links.append((crops["Potato"], diseases["Late Blight"]))
    if "Potato" in crops and "Early Blight" in diseases:
        crop_disease_links.append((crops["Potato"], diseases["Early Blight"]))
    if "Potato" in crops and "Bacterial Wilt" in diseases:
        crop_disease_links.append((crops["Potato"], diseases["Bacterial Wilt"]))
    
    # Mango diseases
    if "Mango" in crops and "Anthracnose" in diseases:
        crop_disease_links.append((crops["Mango"], diseases["Anthracnose"]))
    if "Mango" in crops and "Powdery Mildew" in diseases:
        crop_disease_links.append((crops["Mango"], diseases["Powdery Mildew"]))
    if "Mango" in crops and "Fruit Fly" in diseases:
        crop_disease_links.append((crops["Mango"], diseases["Fruit Fly"]))
    
    # Banana diseases
    if "Banana" in crops and "Panama Wilt" in diseases:
        crop_disease_links.append((crops["Banana"], diseases["Panama Wilt"]))
    if "Banana" in crops and "Sigatoka Leaf Spot" in diseases:
        crop_disease_links.append((crops["Banana"], diseases["Sigatoka Leaf Spot"]))
    
    cursor.executemany(
        "INSERT OR IGNORE INTO crop_diseases (crop_id, disease_id) VALUES (?, ?)",
        crop_disease_links
    )
    conn.commit()
    print("✓ Crop-Diseases relationships populated")

def populate_crop_regions(conn):
    """Populate crop-regions junction table"""
    cursor = conn.cursor()
    
    # Get crop and region IDs
    cursor.execute("SELECT crop_id, crop_name FROM crops")
    crops = dict(cursor.fetchall())
    
    cursor.execute("SELECT region_id, region_name FROM regions")
    regions = dict(cursor.fetchall())
    
    crop_region_links = []
    
    # Rice regions
    if "Rice" in crops and "Punjab" in regions:
        crop_region_links.append((crops["Rice"], regions["Punjab"], 9))
    if "Rice" in crops and "West Bengal" in regions:
        crop_region_links.append((crops["Rice"], regions["West Bengal"], 10))
    if "Rice" in crops and "Tamil Nadu" in regions:
        crop_region_links.append((crops["Rice"], regions["Tamil Nadu"], 9))
    if "Rice" in crops and "Andhra Pradesh" in regions:
        crop_region_links.append((crops["Rice"], regions["Andhra Pradesh"], 10))
    if "Rice" in crops and "Karnataka" in regions:
        crop_region_links.append((crops["Rice"], regions["Karnataka"], 8))
    
    # Wheat regions
    if "Wheat" in crops and "Punjab" in regions:
        crop_region_links.append((crops["Wheat"], regions["Punjab"], 10))
    if "Wheat" in crops and "Haryana" in regions:
        crop_region_links.append((crops["Wheat"], regions["Haryana"], 10))
    if "Wheat" in crops and "Uttar Pradesh" in regions:
        crop_region_links.append((crops["Wheat"], regions["Uttar Pradesh"], 9))
    if "Wheat" in crops and "Madhya Pradesh" in regions:
        crop_region_links.append((crops["Wheat"], regions["Madhya Pradesh"], 8))
    if "Wheat" in crops and "Rajasthan" in regions:
        crop_region_links.append((crops["Wheat"], regions["Rajasthan"], 7))
    
    # Maize regions
    if "Maize" in crops and "Karnataka" in regions:
        crop_region_links.append((crops["Maize"], regions["Karnataka"], 9))
    if "Maize" in crops and "Andhra Pradesh" in regions:
        crop_region_links.append((crops["Maize"], regions["Andhra Pradesh"], 9))
    if "Maize" in crops and "Maharashtra" in regions:
        crop_region_links.append((crops["Maize"], regions["Maharashtra"], 8))
    
    # Cotton regions
    if "Cotton" in crops and "Gujarat" in regions:
        crop_region_links.append((crops["Cotton"], regions["Gujarat"], 10))
    if "Cotton" in crops and "Maharashtra" in regions:
        crop_region_links.append((crops["Cotton"], regions["Maharashtra"], 9))
    if "Cotton" in crops and "Andhra Pradesh" in regions:
        crop_region_links.append((crops["Cotton"], regions["Andhra Pradesh"], 8))
    if "Cotton" in crops and "Punjab" in regions:
        crop_region_links.append((crops["Cotton"], regions["Punjab"], 8))
    
    # Sugarcane regions
    if "Sugarcane" in crops and "Uttar Pradesh" in regions:
        crop_region_links.append((crops["Sugarcane"], regions["Uttar Pradesh"], 10))
    if "Sugarcane" in crops and "Maharashtra" in regions:
        crop_region_links.append((crops["Sugarcane"], regions["Maharashtra"], 9))
    if "Sugarcane" in crops and "Karnataka" in regions:
        crop_region_links.append((crops["Sugarcane"], regions["Karnataka"], 9))
    if "Sugarcane" in crops and "Tamil Nadu" in regions:
        crop_region_links.append((crops["Sugarcane"], regions["Tamil Nadu"], 10))
    
    # Mango regions
    if "Mango" in crops and "Uttar Pradesh" in regions:
        crop_region_links.append((crops["Mango"], regions["Uttar Pradesh"], 10))
    if "Mango" in crops and "Andhra Pradesh" in regions:
        crop_region_links.append((crops["Mango"], regions["Andhra Pradesh"], 10))
    if "Mango" in crops and "Karnataka" in regions:
        crop_region_links.append((crops["Mango"], regions["Karnataka"], 9))
    
    # Banana regions
    if "Banana" in crops and "Maharashtra" in regions:
        crop_region_links.append((crops["Banana"], regions["Maharashtra"], 10))
    if "Banana" in crops and "Tamil Nadu" in regions:
        crop_region_links.append((crops["Banana"], regions["Tamil Nadu"], 10))
    if "Banana" in crops and "Karnataka" in regions:
        crop_region_links.append((crops["Banana"], regions["Karnataka"], 9))
    
    cursor.executemany(
        "INSERT OR IGNORE INTO crop_regions (crop_id, region_id, suitability_score) VALUES (?, ?, ?)",
        crop_region_links
    )
    conn.commit()
    print("✓ Crop-Regions relationships populated")

def initialize_database():
    """Main function to initialize and populate the database"""
    print("=" * 60)
    print("AgriGuard AI Database Initialization")
    print("=" * 60)
    
    # Read and execute schema
    schema_path = os.path.join(BASE_DIR, 'schema.sql')
    with open(schema_path, 'r') as f:
        schema_sql = f.read()
    
    conn = create_connection()
    
    # Create tables
    conn.executescript(schema_sql)
    conn.commit()
    print("✓ Database tables created")
    
    # Populate data
    populate_seasons(conn)
    populate_regions(conn)
    populate_crops(conn)
    populate_crop_parameters(conn)
    populate_diseases(conn)
    populate_crop_diseases(conn)
    populate_crop_regions(conn)
    
    # Verify data
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM crops")
    crop_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM diseases")
    disease_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM regions")
    region_count = cursor.fetchone()[0]
    
    print("\n" + "=" * 60)
    print("Database Initialization Complete!")
    print("=" * 60)
    print(f"📊 Total Crops: {crop_count}")
    print(f"🦠 Total Diseases: {disease_count}")
    print(f"📍 Total Regions: {region_count}")
    print(f"💾 Database Location: {DB_PATH}")
    print("=" * 60)
    
    conn.close()

if __name__ == "__main__":
    initialize_database()

