"""
AgriGuard AI - Additional Database Population
Populates government schemes, NGOs, and suppliers
"""

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'agriguard.db')

def create_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def populate_government_schemes(conn):
    """Populate government schemes table"""
    schemes = [
        ("PM-KISAN Samman Nidhi", "Ministry of Agriculture & Farmers Welfare",
         "Direct income support to farmers - ₹6000/year paid in 3 installments",
         "₹6,000/year", "All landholding farmer families", 
         "https://pmkisan.gov.in", "1800-11-3377", "pmkisan-helpdesk@gov.in"),
        
        ("Fasal Bima Yojana", "Ministry of Agriculture & Farmers Welfare",
         "Crop insurance scheme covering yield losses due to natural calamities",
         "Up to 100% sum insured", "All farmers including sharecroppers",
         "https://pmfby.gov.in", "1800-11-3377", "helpdesk@pmfby.gov.in"),
        
        ("PM-KUSUM Scheme", "Ministry of New and Renewable Energy",
         "Solar pumps for irrigation and grid-connected solar power plants",
         "Up to 90% subsidy", "Farmers with irrigation needs",
         "https://mnre.gov.in", "1800-180-3333", "info@mnre.gov.in"),
        
        ("Kisan Credit Card", "Ministry of Agriculture & Farmers Welfare",
         "Easy credit for farmers at low interest rates for agricultural needs",
         "Up to ₹3 Lakhs", "All farmers - individual/joint borrowers",
         "https://kbckcc.gov.in", "1800-11-3377", "kcc-helpdesk@nabard.org"),
        
        ("National Agricultural Extension Programme", "Ministry of Agriculture",
         "Technology dissemination and training for modern farming practices",
         "Free training", "All farmers", 
         "https://farmer.gov.in", "011-23381092", "extn@agricoop.nic.in"),
        
        ("Paramparagat Krishi Vikas Yojana", "Ministry of Agriculture",
         "Promotion of organic farming through cluster approach",
         "₹20,000/acre", "Farmer groups/PGGs",
         "https://pkvsy.gov.in", "011-23382751", "pkvsy@nic.in"),
        
        ("Micro Irrigation Scheme", "Ministry of Agriculture",
         "Subsidy for drip and sprinkler irrigation systems",
         "55-60% subsidy", "All farmers", 
         "https://microirrigation.gov.in", "011-26536152", "mi-pib@nic.in"),
        
        ("Agricultural Infrastructure Fund", "Ministry of Agriculture",
         "Loans for post-harvest management and infrastructure",
         "3% interest subvention", "FPOs, cooperatives, entrepreneurs",
         "https://aif.msme.gov.in", "1800-11-3377", "aif-helpdesk@nic.in"),
    ]
    
    cursor = conn.cursor()
    cursor.executemany(
        """INSERT OR IGNORE INTO government_schemes 
           (scheme_name, department, description, benefit_amount, eligibility, website, phone, email) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        schemes
    )
    conn.commit()
    print("✓ Government schemes populated")

def populate_ngos(conn):
    """Populate NGOs table"""
    ngos = [
        ("Green Earth Foundation", 
         "Provides organic farming training and free seeds to small farmers. Focus on sustainable agriculture practices.",
         "Training & Seeds", "Pan India", "info@greenearth.org", "+91 98765 43210", "https://greenearth.org"),
        
        ("Farmers First Alliance",
         "Micro-finance support and technical assistance for rural farmers. Helps with market access and fair pricing.",
         "Micro-finance", "Rural Areas", "support@farmersfirst.org", "+91 98765 12345", "https://farmersfirst.org"),
        
        ("Water for All Initiative",
         "Installation of rainwater harvesting systems and drip irrigation. Drought-resistant farming techniques training.",
         "Irrigation Support", "Drought-prone Areas", "help@waterforall.org", "+91 94567 89012", "https://waterforall.org"),
        
        ("Agri-Education Trust",
         "Free agricultural education and modern farming techniques. Women's empowerment through farming cooperatives.",
         "Education & Training", "All States", "learn@agriedu.org", "+91 87654 32109", "https://agriedu.org"),
        
        ("Sustainable Farming Collective",
         "Promotes natural farming methods and provides certification support for organic produce.",
         "Organic Certification", "All India", "contact@sustainablefarming.org", "+91 91234 56789", "https://sustainablefarming.org"),
        
        ("Rural Development Foundation",
         "Comprehensive support for small and marginal farmers including credit, inputs, and market linkage.",
         "Integrated Support", "Rural India", "help@ruraldev.org", "+91 99887 76655", "https://ruraldevfoundation.org"),
    ]
    
    cursor = conn.cursor()
    cursor.executemany(
        """INSERT OR IGNORE INTO ngos 
           (ngo_name, description, program_type, coverage, contact_email, phone, website) 
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ngos
    )
    conn.commit()
    print("✓ NGOs populated")

def populate_suppliers(conn):
    """Populate suppliers table"""
    suppliers = [
        ("AgriChem Solutions", "Urea, DAP, NPK, Organic", "District HQ", "Yes", "Free", 
         "+91 98765 43210", "sales@agrichem.com", 4.8),
        
        ("Farm King Agro", "Urea, Potash, Vermicompost, Pesticides", "Taluka Center", "Yes", "₹100",
         "+91 98765 12345", "info@farmking.com", 4.2),
        
        ("GreenGrow Fertilizers", "Organic, Bio-fertilizers, Compost, Micronutrients", "Block HQ", "Yes", "Free",
         "+91 94567 89012", "contact@greengrow.com", 4.9),
        
        ("Krishi Bazar", "Urea, DAP, SSP, Insecticides", "Village Market", "No", "Pickup Only",
         "+91 87654 32109", "orders@krishibazar.com", 3.9),
        
        ("AgroTech India", "NPK, Urea, DAP, Pesticides, Herbicides", "State Capital", "Yes", "₹50",
         "+91 90123 45678", "sales@agrotechindia.com", 4.5),
        
        ("BioFarms Organic", "Organic fertilizers, Vermicompost, Neem cake, Bone meal", "Metro City", "Yes", "Free",
         "+91 81234 56790", "info@biofarms.com", 4.7),
        
        ("CropCare Distributors", "All types of fertilizers, Pesticides, Seeds", "Warehouse Hub", "Yes", "₹75",
         "+91 78901 23456", "orders@cropcare.com", 4.3),
        
        ("Desi Krishi Store", "Traditional organic inputs, Cow dung, Compost", "Rural Market", "Yes", "Free",
         "+91 98765 00011", "desikrishi@gmail.com", 4.6),
    ]
    
    cursor = conn.cursor()
    cursor.executemany(
        """INSERT OR IGNORE INTO suppliers 
           (supplier_name, products, location, delivery_available, delivery_charge, phone, email, rating) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        suppliers
    )
    conn.commit()
    print("✓ Suppliers populated")

def populate_extra_data():
    """Populate the new tables"""
    conn = create_connection()
    
    # Add the new tables
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS government_schemes (
            scheme_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scheme_name TEXT NOT NULL,
            department TEXT,
            description TEXT,
            benefit_amount TEXT,
            eligibility TEXT,
            website TEXT,
            phone TEXT,
            email TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ngos (
            ngo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngo_name TEXT NOT NULL,
            description TEXT,
            program_type TEXT,
            coverage TEXT,
            contact_email TEXT,
            phone TEXT,
            website TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT NOT NULL,
            products TEXT,
            location TEXT,
            delivery_available TEXT,
            delivery_charge TEXT,
            phone TEXT,
            email TEXT,
            rating REAL DEFAULT 4.0
        )
    """)
    
    conn.commit()
    print("✓ New tables created")
    
    # Populate data
    populate_government_schemes(conn)
    populate_ngos(conn)
    populate_suppliers(conn)
    
    # Verify
    cursor.execute("SELECT COUNT(*) FROM government_schemes")
    scheme_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ngos")
    ngo_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM suppliers")
    supplier_count = cursor.fetchone()[0]
    
    print("\n" + "=" * 50)
    print("Extra Data Population Complete!")
    print("=" * 50)
    print(f"🏛️ Government Schemes: {scheme_count}")
    print(f"🤝 NGOs: {ngo_count}")
    print(f"🏪 Suppliers: {supplier_count}")
    print("=" * 50)
    
    conn.close()

if __name__ == "__main__":
    populate_extra_data()

