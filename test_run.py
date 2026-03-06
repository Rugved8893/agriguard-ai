import sys
sys.path.insert(0, 'c:/Users/HP/OneDrive/Documents/Desktop/AgricultureManagement System')

# Import the database utility
from database.db_util import get_all_crops, get_crop_parameters, calculate_risk

print("=== Testing Database Functions ===")
crops = get_all_crops()
print(f"Total Crops: {len(crops)}")

# Test with Rice
params = get_crop_parameters("Rice")
print(f"\nRice Parameters: {params}")

# Test risk calculation
risk = calculate_risk(150, 28, 75, 6.5, "Rice")
print(f"\nRisk for Rice: {risk}")

print("\n=== Starting Flask App ===")
from app import app
app.run(debug=True, port=5000)
