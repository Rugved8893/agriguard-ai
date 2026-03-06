-- AgriGuard AI Database Schema
-- SQLite Database for Agricultural Management System

-- Drop tables if they exist (for fresh setup)
DROP TABLE IF EXISTS crop_diseases;
DROP TABLE IF EXISTS diseases;
DROP TABLE IF EXISTS crop_parameters;
DROP TABLE IF EXISTS crops;
DROP TABLE IF EXISTS seasons;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS government_schemes;
DROP TABLE IF EXISTS ngos;
DROP TABLE IF EXISTS suppliers;

-- ============================================
-- REGIONS TABLE
-- ============================================
CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_name TEXT NOT NULL UNIQUE,
    climate_type TEXT,
    avg_rainfall_mm INTEGER,
    description TEXT
);

-- ============================================
-- SEASONS TABLE
-- ============================================
CREATE TABLE seasons (
    season_id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_name TEXT NOT NULL UNIQUE,
    months TEXT NOT NULL,
    monsoon_active INTEGER DEFAULT 0,
    rain_likely INTEGER DEFAULT 0,
    description TEXT
);

-- ============================================
-- CROPS TABLE
-- ============================================
CREATE TABLE crops (
    crop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    season_id INTEGER,
    water_need TEXT,
    nutrient_need TEXT,
    sowing_period TEXT,
    harvest_period TEXT,
    yield_min REAL,
    yield_max REAL,
    yield_unit TEXT,
    description TEXT,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);

-- ============================================
-- CROP PARAMETERS TABLE
-- ============================================
CREATE TABLE crop_parameters (
    param_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    param_type TEXT NOT NULL,
    rainfall_min_mm INTEGER,
    rainfall_max_mm INTEGER,
    temp_min_c REAL,
    temp_max_c REAL,
    humidity_min INTEGER,
    humidity_max INTEGER,
    ph_min REAL,
    ph_max REAL,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id) ON DELETE CASCADE
);

-- ============================================
-- DISEASES TABLE
-- ============================================
CREATE TABLE diseases (
    disease_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_name TEXT NOT NULL UNIQUE,
    disease_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    symptoms TEXT,
    conditions_favoured TEXT,
    treatment_chemical TEXT,
    treatment_organic TEXT,
    prevention TEXT
);

-- ============================================
-- CROP DISEASES JUNCTION TABLE
-- ============================================
CREATE TABLE crop_diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    disease_id INTEGER NOT NULL,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id) ON DELETE CASCADE,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE,
    UNIQUE(crop_id, disease_id)
);

-- ============================================
-- CROP REGIONS JUNCTION TABLE
-- ============================================
CREATE TABLE crop_regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    region_id INTEGER NOT NULL,
    suitability_score INTEGER DEFAULT 5,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id) ON DELETE CASCADE,
    FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE CASCADE,
    UNIQUE(crop_id, region_id)
);

-- ============================================
-- GOVERNMENT SCHEMES TABLE
-- ============================================
CREATE TABLE government_schemes (
    scheme_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_name TEXT NOT NULL,
    department TEXT,
    description TEXT,
    benefit_amount TEXT,
    eligibility TEXT,
    website TEXT,
    phone TEXT,
    email TEXT
);

-- ============================================
-- NGO TABLE
-- ============================================
CREATE TABLE ngos (
    ngo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ngo_name TEXT NOT NULL,
    description TEXT,
    program_type TEXT,
    coverage TEXT,
    contact_email TEXT,
    phone TEXT,
    website TEXT
);

-- ============================================
-- SUPPLIERS TABLE
-- ============================================
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL,
    products TEXT,
    location TEXT,
    delivery_available TEXT,
    delivery_charge TEXT,
    phone TEXT,
    email TEXT,
    rating REAL DEFAULT 4.0
);

-- ============================================
-- INDEXES FOR BETTER PERFORMANCE
-- ============================================
CREATE INDEX idx_crops_category ON crops(category);
CREATE INDEX idx_crops_season ON crops(season_id);
CREATE INDEX idx_crop_parameters_crop ON crop_parameters(crop_id);
CREATE INDEX idx_diseases_type ON diseases(disease_type);
CREATE INDEX idx_crop_diseases_crop ON crop_diseases(crop_id);
CREATE INDEX idx_crop_diseases_disease ON crop_diseases(disease_id);

