"""
AgriGuard AI Database Utility Module
Provides functions to interact with the SQLite database
"""

import sqlite3
import os

# Database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'agriguard.db')

def get_connection():
    """Get a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_crops():
    """Get all crops from database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, s.season_name 
        FROM crops c 
        LEFT JOIN seasons s ON c.season_id = s.season_id
        ORDER BY c.category, c.crop_name
    """)
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_crops_by_category(category):
    """Get crops by category"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, s.season_name 
        FROM crops c 
        LEFT JOIN seasons s ON c.season_id = s.season_id
        WHERE c.category = ?
        ORDER BY c.crop_name
    """, (category,))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_crops_by_season(season_name):
    """Get crops by season"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, s.season_name 
        FROM crops c 
        INNER JOIN seasons s ON c.season_id = s.season_id
        WHERE s.season_name = ?
        ORDER BY c.crop_name
    """, (season_name,))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_crop_by_name(crop_name):
    """Get crop details by name"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, s.season_name 
        FROM crops c 
        LEFT JOIN seasons s ON c.season_id = s.season_id
        WHERE c.crop_name = ?
    """, (crop_name,))
    row = cursor.fetchone()
    result = dict(row) if row else None
    conn.close()
    return result

def get_crop_parameters(crop_name):
    """Get optimal and tolerance parameters for a crop"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get crop_id
    cursor.execute("SELECT crop_id FROM crops WHERE crop_name = ?", (crop_name,))
    crop_row = cursor.fetchone()
    
    if not crop_row:
        conn.close()
        return None
    
    crop_id = crop_row['crop_id']
    
    # Get parameters
    cursor.execute("""
        SELECT * FROM crop_parameters 
        WHERE crop_id = ? AND param_type = 'optimal'
    """, (crop_id,))
    optimal = dict(cursor.fetchone()) if cursor.fetchone() else None
    
    cursor.execute("""
        SELECT * FROM crop_parameters 
        WHERE crop_id = ? AND param_type = 'tolerance'
    """, (crop_id,))
    tolerance = dict(cursor.fetchone()) if cursor.fetchone() else None
    
    # Re-fetch optimal (cursor was consumed)
    cursor.execute("""
        SELECT * FROM crop_parameters 
        WHERE crop_id = ? AND param_type = 'optimal'
    """, (crop_id,))
    optimal = dict(cursor.fetchone()) if cursor.fetchone() else None
    
    conn.close()
    
    return {
        "optimal": optimal,
        "tolerance": tolerance
    }

def get_crop_diseases(crop_name):
    """Get diseases for a specific crop"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT d.* FROM diseases d
        INNER JOIN crop_diseases cd ON d.disease_id = cd.disease_id
        INNER JOIN crops c ON cd.crop_id = c.crop_id
        WHERE c.crop_name = ?
    """, (crop_name,))
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_crop_regions(crop_name):
    """Get suitable regions for a specific crop"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT r.*, cr.suitability_score 
        FROM regions r
        INNER JOIN crop_regions cr ON r.region_id = cr.region_id
        INNER JOIN crops c ON cr.crop_id = c.crop_id
        WHERE c.crop_name = ?
        ORDER BY cr.suitability_score DESC
    """, (crop_name,))
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_all_diseases():
    """Get all diseases"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diseases ORDER BY disease_name")
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_disease_by_name(disease_name):
    """Get disease details by name"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diseases WHERE disease_name = ?", (disease_name,))
    row = cursor.fetchone()
    result = dict(row) if row else None
    conn.close()
    return result

def get_diseases_by_type(disease_type):
    """Get diseases by type (Fungal, Bacterial, Viral, Insect)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM diseases 
        WHERE disease_type = ? 
        ORDER BY severity DESC, disease_name
    """, (disease_type,))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_all_regions():
    """Get all regions"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM regions ORDER BY region_name")
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_all_seasons():
    """Get all seasons"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasons ORDER BY season_id")
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def calculate_risk(rainfall, temperature, humidity, soil_ph, crop_name):
    """Calculate risk level based on crop parameters"""
    params = get_crop_parameters(crop_name)
    
    if not params or not params.get('optimal'):
        return {"error": "Crop not found"}
    
    optimal = params['optimal']
    tolerance = params['tolerance']
    
    risks = {}
    total_risk = 0
    
    # Rainfall risk
    rain_risk = 0
    rain_reason = "Optimal"
    if rainfall < optimal['rainfall_min_mm']:
        deficit = optimal['rainfall_min_mm'] - rainfall
        if deficit > 100:
            rain_risk = 25
            rain_reason = "Critical water shortage"
        elif deficit > 50:
            rain_risk = 15
            rain_reason = "Water deficit"
        else:
            rain_risk = 8
            rain_reason = "Slightly below optimal"
    elif rainfall > optimal['rainfall_max_mm']:
        excess = rainfall - optimal['rainfall_max_mm']
        if excess > 100:
            rain_risk = 20
            rain_reason = "Excessive rainfall - waterlogging risk"
        else:
            rain_risk = 10
            rain_reason = "Above optimal rainfall"
    
    risks['rainfall'] = {'score': rain_risk, 'reason': rain_reason, 'value': rainfall}
    total_risk += rain_risk
    
    # Temperature risk
    temp_risk = 0
    temp_reason = "Optimal"
    if temperature < optimal['temp_min_c']:
        if temperature < optimal['temp_min_c'] - 10:
            temp_risk = 20
            temp_reason = "Cold stress"
        else:
            temp_risk = 10
            temp_reason = "Below optimal temperature"
    elif temperature > optimal['temp_max_c']:
        if temperature > optimal['temp_max_c'] + 8:
            temp_risk = 25
            temp_reason = "Extreme heat stress"
        elif temperature > optimal['temp_max_c'] + 5:
            temp_risk = 18
            temp_reason = "Heat stress"
        else:
            temp_risk = 10
            temp_reason = "Above optimal temperature"
    
    risks['temperature'] = {'score': temp_risk, 'reason': temp_reason, 'value': temperature}
    total_risk += temp_risk
    
    # Humidity risk
    hum_risk = 0
    hum_reason = "Optimal"
    if humidity < optimal['humidity_min']:
        if humidity < optimal['humidity_min'] - 20:
            hum_risk = 15
            hum_reason = "Very low humidity - moisture stress"
        else:
            hum_risk = 8
            hum_reason = "Below optimal humidity"
    elif humidity > optimal['humidity_max']:
        if humidity > 90:
            hum_risk = 15
            hum_reason = "Very high humidity - disease risk"
        else:
            hum_risk = 8
            hum_reason = "Above optimal humidity"
    
    risks['humidity'] = {'score': hum_risk, 'reason': hum_reason, 'value': humidity}
    total_risk += hum_risk
    
    # Soil pH risk
    ph_risk = 0
    ph_reason = "Optimal"
    ideal_ph = (optimal['ph_min'] + optimal['ph_max']) / 2
    ph_diff = soil_ph - ideal_ph
    
    if abs(ph_diff) > 2.0:
        ph_risk = 20
        ph_reason = f"Soil pH {soil_ph} severely outside optimal"
    elif abs(ph_diff) > 1.0:
        ph_risk = 10
        ph_reason = f"Soil pH {soil_ph} slightly outside optimal"
    elif abs(ph_diff) > 0.5:
        ph_risk = 3
        ph_reason = "Minor pH deviation"
    
    risks['soil_ph'] = {'score': ph_risk, 'reason': ph_reason, 'value': soil_ph}
    total_risk += ph_risk
    
    # Determine risk level
    weighted_risk = (
        risks['rainfall']['score'] * 1.2 +
        risks['temperature']['score'] * 1.3 +
        risks['humidity']['score'] * 1.0 +
        risks['soil_ph']['score'] * 0.8
    )
    
    if weighted_risk >= 70:
        risk_level = "CRITICAL"
        loss_estimate = "70-90%"
    elif weighted_risk >= 45:
        risk_level = "HIGH RISK"
        loss_estimate = "40-60%"
    elif weighted_risk >= 25:
        risk_level = "MODERATE"
        loss_estimate = "15-30%"
    else:
        risk_level = "OPTIMAL"
        loss_estimate = "0-10%"
    
    return {
        "risk_level": risk_level,
        "estimated_loss": loss_estimate,
        "total_risk_score": total_risk,
        "weighted_risk_score": weighted_risk,
        "risks": risks,
        "optimal_parameters": {
            "rainfall": f"{optimal['rainfall_min_mm']}-{optimal['rainfall_max_mm']}mm",
            "temperature": f"{optimal['temp_min_c']}-{optimal['temp_max_c']}°C",
            "humidity": f"{optimal['humidity_min']}-{optimal['humidity_max']}%",
            "soil_ph": f"{optimal['ph_min']}-{optimal['ph_max']}"
        }
    }

def search_crops(query):
    """Search crops by name"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, s.season_name 
        FROM crops c 
        LEFT JOIN seasons s ON c.season_id = s.season_id
        WHERE c.crop_name LIKE ?
        ORDER BY c.crop_name
    """, (f"%{query}%",))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_dashboard_stats():
    """Get statistics for dashboard"""
    conn = get_connection()
    cursor = conn.cursor()
    
    stats = {}
    
    cursor.execute("SELECT COUNT(*) FROM crops")
    stats['total_crops'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM diseases")
    stats['total_diseases'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM regions")
    stats['total_regions'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM government_schemes")
    stats['total_schemes'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM ngos")
    stats['total_ngos'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM suppliers")
    stats['total_suppliers'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT category, COUNT(*) as count FROM crops GROUP BY category")
    stats['crops_by_category'] = {row['category']: row['count'] for row in cursor.fetchall()}
    
    cursor.execute("SELECT disease_type, COUNT(*) as count FROM diseases GROUP BY disease_type")
    stats['diseases_by_type'] = {row['disease_type']: row['count'] for row in cursor.fetchall()}
    
    conn.close()
    return stats

# ===== NEW FUNCTIONS FOR GOVERNMENT SCHEMES, NGOS, AND SUPPLIERS =====

def get_all_government_schemes():
    """Get all government schemes"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM government_schemes ORDER BY scheme_name")
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_government_scheme_by_id(scheme_id):
    """Get government scheme by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM government_schemes WHERE scheme_id = ?", (scheme_id,))
    row = cursor.fetchone()
    result = dict(row) if row else None
    conn.close()
    return result

def get_all_ngos():
    """Get all NGOs"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ngos ORDER BY ngo_name")
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_ngo_by_id(ngo_id):
    """Get NGO by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ngos WHERE ngo_id = ?", (ngo_id,))
    row = cursor.fetchone()
    result = dict(row) if row else None
    conn.close()
    return result

def get_all_suppliers():
    """Get all suppliers"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers ORDER BY rating DESC")
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_supplier_by_id(supplier_id):
    """Get supplier by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers WHERE supplier_id = ?", (supplier_id,))
    row = cursor.fetchone()
    result = dict(row) if row else None
    conn.close()
    return result

def search_suppliers(product_query):
    """Search suppliers by products"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM suppliers 
        WHERE products LIKE ?
        ORDER BY rating DESC
    """, (f"%{product_query}%",))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results


# Test the database functions
if __name__ == "__main__":
    print("Testing Database Functions...")
    print("=" * 50)
    
    # Test get_all_crops
    crops = get_all_crops()
    print(f"Total Crops: {len(crops)}")
    
    # Test get_crop_by_name
    rice = get_crop_by_name("Rice")
    if rice:
        print(f"\nRice Details:")
        print(f"  Category: {rice['category']}")
        print(f"  Season: {rice['season_name']}")
        print(f"  Water Need: {rice['water_need']}")
        print(f"  Yield: {rice['yield_min']}-{rice['yield_max']} {rice['yield_unit']}")
    
    # Test dashboard stats
    stats = get_dashboard_stats()
    print(f"\nDashboard Statistics:")
    print(f"  Total Crops: {stats['total_crops']}")
    print(f"  Total Diseases: {stats['total_diseases']}")
    print(f"  Total Regions: {stats['total_regions']}")
    print(f"  Total Schemes: {stats.get('total_schemes', 0)}")
    print(f"  Total NGOs: {stats.get('total_ngos', 0)}")
    print(f"  Total Suppliers: {stats.get('total_suppliers', 0)}")
    print(f"  Crops by Category: {stats['crops_by_category']}")
    
    # Test government schemes
    schemes = get_all_government_schemes()
    print(f"\nGovernment Schemes: {len(schemes)}")
    if schemes:
        print(f"  First scheme: {schemes[0]['scheme_name']}")
    
    # Test NGOs
    ngos = get_all_ngos()
    print(f"\nNGOs: {len(ngos)}")
    if ngos:
        print(f"  First NGO: {ngos[0]['ngo_name']}")
    
    # Test suppliers
    suppliers = get_all_suppliers()
    print(f"\nSuppliers: {len(suppliers)}")
    if suppliers:
        print(f"  First supplier: {suppliers[0]['supplier_name']}")
    
    print("\n" + "=" * 50)
    print("Database Functions Test Complete!")

