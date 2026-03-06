import sqlite3

DB_PATH = "c:/Users/HP/OneDrive/Documents/Desktop/AgricultureManagement System/database/agriguard.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check crops table
print("=== CROPS TABLE ===")
cur.execute("SELECT crop_id, crop_name, category FROM crops LIMIT 5")
for row in cur.fetchall():
    print(row)

print("\n=== CROP PARAMETERS TABLE ===")
cur.execute("SELECT * FROM crop_parameters LIMIT 10")
for row in cur.fetchall():
    print(row)

print("\n=== CHECKING RICE SPECIFICALLY ===")
cur.execute("SELECT crop_id FROM crops WHERE crop_name = 'Rice'")
rice_id = cur.fetchone()
print(f"Rice crop_id: {rice_id}")

if rice_id:
    cur.execute("SELECT * FROM crop_parameters WHERE crop_id = ?", (rice_id[0],))
    params = cur.fetchall()
    print(f"Rice parameters: {params}")

conn.close()

