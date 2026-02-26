"""
AgriGuard AI - Comprehensive Farming Knowledge Base
This provides detailed, expert-level responses for farmer queries
"""

import random
from datetime import datetime

class AIFarmingAssistant:
    """Intelligent Farming Assistant with extensive agricultural knowledge"""
    
    def __init__(self):
        self.language = "en"
        
    def set_language(self, lang_code):
        """Set the response language"""
        self.language = lang_code
        
    def get_response(self, query, crop_type=None, environmental_data=None):
        """
        Generate comprehensive AI response based on user query
        Similar to ChatGPT - provides detailed, contextual responses
        """
        query_lower = query.lower()
        
        # Route to appropriate knowledge base
        if any(word in query_lower for word in ['disease', 'infection', 'fungal', 'bacterial', 'pest', 'bug', 'blight']):
            return self._get_disease_info(query, crop_type)
        elif any(word in query_lower for word in ['fertilizer', 'nutrient', 'npk', 'urea', 'dap', 'manure', ' compost']):
            return self._get_fertilizer_info(query, crop_type)
        elif any(word in query_lower for word in ['water', 'irrigation', 'rain', 'drought', 'flood']):
            return self._get_water_info(query, crop_type)
        elif any(word in query_lower for word in ['temperature', 'heat', 'cold', 'climate', 'weather']):
            return self._get_climate_info(query, crop_type)
        elif any(word in query_lower for word in ['soil', 'ph', 'acid', 'alkaline', 'ground']):
            return self._get_soil_info(query, crop_type)
        elif any(word in query_lower for word in ['yield', 'production', 'harvest', 'profit', 'income']):
            return self._get_yield_info(query, crop_type)
        elif any(word in query_lower for word in ['plant', 'seed', 'sow', 'planting', 'germination']):
            return self._get_planting_info(query, crop_type)
        elif any(word in query_lower for word in ['hello', 'hi', 'hey', 'greetings', 'namaste']):
            return self._get_greeting()
        elif any(word in query_lower for word in ['help', 'what can you do', 'assist']):
            return self._get_capabilities()
        else:
            return self._get_general_farming_info(query, crop_type)
    
    def _get_greeting(self):
        """Greeting response"""
        greetings = {
            "en": """👋 Namaste! Welcome to AgriGuard AI Assistant!

I'm your personal farming expert, available 24/7 to help you with:

🌾 **Crop Management** - Planting schedules, variety selection, and cultivation techniques
🦠 **Disease & Pest Control** - Identification and organic/chemical treatment solutions
💧 **Irrigation Planning** - Water management and drought/flood preparedness
🧪 **Soil Health** - pH optimization, nutrient management, and fertilizer recommendations
📊 **Yield Optimization** - Techniques to maximize your harvest and profits
🌤️ **Weather Adaptation** - Climate-resilient farming strategies

How can I help you today? Feel free to ask any question about your crops, soil, weather, or farming practices!""",
            
            "hi": """👋 नमस्ते! AgriGuard AI सहायक में आपका स्वागत है!

मैं आपका व्यक्तिगत कृषि विशेषज्ञ हूं, जो आपकी मदद के लिए 24/7 उपलब्ध है:

🌾 **फसल प्रबंधन** - रोपण अनुसूचियां, विविधता चयन और खेती तकनीक
🦠 **रोग एवं कीट नियंत्रण** - पहचान और उपचार समाधान
💧 **सिंचाई योजना** - जल प्रबंधन और सूखा/बाढ़ तैयारी
🧪 **मिट्टी स्वास्थ्य** - pH अनुकूलन, पोषक तत्व प्रबंधन
📊 **उपज अनुकूलन** - अपनी फसल बढ़ाने की तकनीक

आज मैं आपकी कैसे मदद कर सकता हूं?""",
            
            "ta": """👋 வனக்கம்! AgriGuard AI உதவியாளருக்கு வரவேற்கிறோம்!

நான் உங்கள் தனிப்பட்ட விவசாய நிபுணர், 24/7 உதவி:

🌾 **பயிர் மேலாண்மை** - நடவு அட்டவணை, வகை தேர்வு
🦠 **நோய் & பூச்சி கட்டுப்பாடு** - அடையாளம் மற்றும் சிகிச்சை
💧 **நீர்ப்பாசன திட்டம்** - நீர் மேலாண்மை
🧪 **மண் சுகாதாரம்** - pH மேம்பாடு
📊 **விளைச்சல் மேம்பாடு** - அதிகரித்த அறுவடை

இன்று உங்களுக்கு எவ்வாறு உதவ முடியும்?"""
        }
        return greetings.get(self.language, greetings["en"])
    
    def _get_capabilities(self):
        """List AI capabilities"""
        return """🤖 **AgriGuard AI - Your Farming Expert**

I can help you with:

📋 **Comprehensive Crop Advisory**
   - Variety selection based on your soil and climate
   - Planting and harvesting schedules
   - Crop rotation recommendations
   - Intercropping strategies

🦠 **Disease & Pest Management**
   - Identify symptoms from descriptions
   - Organic and chemical treatment options
   - Prevention strategies
   - Integrated Pest Management (IPM)

💧 **Water Management**
   - Irrigation scheduling
   - Drip and sprinkler system guidance
   - Rainwater harvesting
   - Drought management

🧪 **Nutrient Management**
   - Fertilizer recommendations (organic & chemical)
   - NPK calculations
   - Soil amendment strategies
   - Composting techniques

🌡️ **Climate Adaptation**
   - Weather-based advisories
   - Heat/cold stress management
   - Storm and flood protection
   - Seasonal planning

📈 **Economic Advice**
   - Cost reduction strategies
   - Government scheme information
   - Market timing recommendations
   - Profit optimization

Just describe your problem or ask any question - I'll provide detailed, actionable advice!"""
    
    def _get_disease_info(self, query, crop_type):
        """Detailed disease information"""
        diseases = {
            "rice": {
                "name": "Rice",
                "common_diseases": [
                    {
                        "disease": "Blast (Magnaporthe oryzae)",
                        "symptoms": "Diamond-shaped lesions with gray centers on leaves, nodes, and panicles. Lesions can merge and kill entire leaves.",
                        "causes": "High humidity (>90%), moderate temperatures (24-30°C), excessive nitrogen fertilization, drought stress followed by moisture.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Tricyclazole 75% WP @ 0.6 g/L or
• Isoprothiolane 40% EC @ 1.5 ml/L or
• Azoxystrobin 23% SC @ 1.0 ml/L

**Organic:**
• Neem cake application @ 250 kg/acre
• Neem oil spray 5 ml/L
• Trichoderma viride bio-control agent
• Pseudomonas fluorescens seed treatment

**Prevention:**
• Use resistant varieties (IR 64, Swarna, BPT 5204)
• Avoid excessive nitrogen application
• Maintain proper plant spacing
• Remove crop residues
• Drain fields periodically""",
                        "severity": "High - Can cause 50-80% yield loss if untreated"
                    },
                    {
                        "disease": "Bacterial Leaf Blight (Xanthomonas oryzae)",
                        "symptoms": "Yellow to white lesions starting from leaf tips or margins, progressing downward. Lesions have wavy margins and bacterial ooze visible in morning.",
                        "causes": "Warm temperatures (25-30°C), high humidity, wounds from insects/storms, contaminated irrigation water.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Copper Oxychloride 50% WP @ 2.5 g/L
• Streptomycin 90% + Tetracycline 10% @ 0.3 g/L
• Agrimycin-100 @ 0.3 g/L

**Organic:**
• Neem seed kernel extract 5%
• Trichoderma-based formulations
• Good drainage maintenance
• Balanced fertilization

**Prevention:**
• Use certified disease-free seeds
• Avoid working in wet fields
• Control insect vectors
• Use resistant varieties""",
                        "severity": "Severe - Can cause 20-50% yield loss"
                    },
                    {
                        "disease": "Brown Spot (Bipolaris oryzae)",
                        "symptoms": "Brown to dark brown oval spots on leaves, can enlarge and merge. Severe infection causes leaf drying and grain discoloration.",
                        "causes": "Nutrient deficiency (especially nitrogen), drought stress, poor soil health, high humidity.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Mancozeb 75% WP @ 2 g/L
• Propiconazole 25% EC @ 1 ml/L
• Carbendazim 50% WP @ 1 g/L

**Organic:**
• Neem cake application
• Vermicompost application
• Proper nutrient management
• Organic mulching

**Prevention:**
• Maintain adequate nitrogen nutrition
• Use healthy seeds
• Avoid water stress
• Improve soil organic matter""",
                        "severity": "Moderate - Causes 10-30% yield loss"
                    }
                ]
            },
            "wheat": {
                "name": "Wheat",
                "common_diseases": [
                    {
                        "disease": "Rust Diseases (Puccinia spp.)",
                        "symptoms": "Orange/brown pustules on leaves (leaf rust), stem (stem rust), or heads (stripe rust). Pustules rupture releasing powdery spores.",
                        "causes": "Cool, moist conditions (15-25°C), high humidity, presence of alternate hosts, wind-borne spore dispersal.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Propiconazole 25% EC @ 0.5 L/acre
• Tebuconazole 25% EC @ 0.5 L/acre
• Azoxystrobin 23% SC @ 200 ml/acre
• Triademifon 25% WP @ 0.5 kg/acre

**Organic:**
• Sulfur-based organic fungicides
• Neem-based formulations
• Early sowing to avoid peak infection
• Remove volunteer wheat plants

**Prevention:**
• Use rust-resistant varieties
• Early sowing (October in India)
• Monitor fields regularly
• Remove alternate host plants (barberry)""",
                        "severity": "Very High - Can cause 40-100% yield loss in severe epidemics"
                    },
                    {
                        "disease": "Powdery Mildew (Blumeria graminis)",
                        "symptoms": "White to gray powdery coating on leaves, stems, and heads. Leaves may turn yellow and dry under severe infection.",
                        "causes": "Moderate temperatures (15-22°C), low humidity, dense canopy, excessive nitrogen.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Sulfur 80% WDG @ 2 kg/acre
• Propiconazole 25% EC @ 0.5 L/acre
• Tebuconazole 25% EC @ 300 ml/acre
• Dinocap 48% EC @ 0.5 L/acre

**Organic:**
• Neem oil 5 ml/L spray
• Garlic extract spray
• Baking soda solution (1 tbsp/L)
• Milk spray (1:9 with water)

**Prevention:**
• Use resistant varieties
• Adequate plant spacing
• Balanced nitrogen application
• Remove crop debris""",
                        "severity": "Moderate to High - 10-40% yield loss"
                    }
                ]
            },
            "maize": {
                "name": "Maize",
                "common_diseases": [
                    {
                        "disease": "Northern Leaf Blight (Exserohilum turcicum)",
                        "symptoms": "Gray-green to tan elliptical lesions on leaves, often starting from lower leaves. Lesions can coalesce causing extensive leaf damage.",
                        "causes": "Moderate temperatures (18-27°C), high humidity (>90%), prolonged leaf wetness, late sowing.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Mancozeb 75% WP @ 2.5 g/L
• Propiconazole 25% EC @ 1 ml/L
• Azoxystrobin 23% SC @ 1 ml/L
• Tricyclazole 75% WP @ 0.6 g/L

**Organic:**
• Neem cake application
• Crop rotation
• Trichoderma application
• Balanced fertilization

**Prevention:**
• Use resistant hybrids (HQPM 1, PMH 1)
• Early sowing
• Adequate plant spacing
• Remove infected debris""",
                        "severity": "Moderate to High - 20-50% yield loss"
                    },
                    {
                        "disease": "Common Rust (Puccinia sorghi)",
                        "symptoms": "Small, circular to elongate, cinnamon-brown pustules on both leaf surfaces. Pustules contain powdery brown spores.",
                        "causes": "Cool to moderate temperatures (15-25°C), high humidity, late planted crops.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Propiconazole 25% EC @ 0.5 L/acre
• Tebuconazole 25% EC @ 0.5 L/acre
• Mancozeb 75% WP @ 2 kg/acre
• Azoxystrobin 23% SC @ 200 ml/acre

**Organic:**
• Neem oil spray
• Garlic-bud extract
• Early planting
• Remove infected leaves

**Prevention:**
• Use resistant varieties
• Early sowing (by July)
• Scouting early
• Proper plant density""",
                        "severity": "Moderate - 10-30% yield loss"
                    }
                ]
            },
            "sugarcane": {
                "name": "Sugarcane",
                "common_diseases": [
                    {
                        "disease": "Red Rot (Colletotrichum falcatum)",
                        "symptoms": "Reddish lesions with dark margins on leaves, internal stalk rotting with characteristic red and white alternating pattern. Foul odor from infected stalks.",
                        "causes": "High humidity, waterlogged conditions, wounds from insects/harvesting, infected seed material.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Carbendazim 50% WP @ 1 g/L
• Propiconazole 25% EC @ 1 ml/L
• Copper Oxychloride 50% WP @ 2.5 g/L

**Organic:**
• Trichoderma viride application
• Neem cake application
• Remove and burn infected stalks
• Improve drainage

**Prevention:**
• Use disease-free seed material
• Use resistant varieties (Co 86032, Co 99004)
• Avoid wounding during operations
• Crop rotation
• Hot water treatment of seed sets""",
                        "severity": "Very High - 30-70% yield loss and quality decline"
                    },
                    {
                        "disease": "Smut (Sporisorium scitamineum)",
                        "symptoms": "Black, whip-like sori (cushion-like masses) emerging from the growing point. Infected plants become stunted and produce few tillers.",
                        "causes": "Warm temperatures (25-30°C), drought stress, infected seed material, wounds.",
                        "treatment": """🔬 **Treatment Options:**

**Chemical:**
• Apply Propiconazole 25% EC @ 1 ml/L
• Tebuconazole 25% EC @ 1 ml/L
• Carbendazim 50% WP @ 1 g/L (seed treatment)

**Organic:**
• Neem cake application
• Trichoderma seed treatment
• Remove and burn infected plants
• Solar treatment of seed material

**Prevention:**
• Use disease-free seed
• Use resistant varieties
• Rogue infected plants immediately
• Heat treatment of seed sets (50°C for 2 hours)""",
                        "severity": "High - 20-60% yield loss"
                    }
                ]
            }
        }
        
        # If crop type specified, provide detailed info
        if crop_type and crop_type.lower() in diseases:
            crop_info = diseases[crop_type.lower()]
            return f"""🌾 **{crop_info['name']} Disease Guide**

I found detailed information about common diseases in {crop_info['name']}:

"""
        
        # General disease response
        return f"""🦠 **Plant Disease Information**

To provide you with detailed disease information, please specify:

1. **Crop Type** - Which crop is affected (Rice, Wheat, Maize, Sugarcane, Cotton, etc.)?

2. **Visible Symptoms** - Describe what you see:
   • Color changes (yellow, brown, black spots)
   • Wilting or drooping
   • Unusual growths or formations
   • Leaf curling or deformation

3. **Affected Parts** - Which plant parts are affected?
   • Leaves, stems, roots, fruits, or flowers

Once you provide these details, I can give you:
- ✅ Accurate disease identification
- 🧪 Chemical treatment options
- 🌿 Organic/natural remedies
- 🛡️ Prevention strategies
- 📊 Severity assessment

What crop and symptoms are you observing?"""
    
    def _get_fertilizer_info(self, query, crop_type):
        """Detailed fertilizer recommendations"""
        return f"""🧪 **Comprehensive Fertilizer Guide**

## Understanding NPK:

**N (Nitrogen)** - Promotes leafy growth and green color
- Deficiency: Yellowing leaves from bottom up, stunted growth
- Excess: Excessive leaf growth, delayed maturity, pest attraction

**P (Phosphorus)** - Root development and flowering
- Deficiency: Purple/reddish leaves, poor root growth
- Excess: Zinc/iron deficiency, environmental issues

**K (Potassium)** - Overall plant health and disease resistance
- Deficiency: Brown leaf edges, weak stems
- Excess: Calcium/magnesium deficiency

## Crop-Specific Recommendations:

### Rice:
- **Basal (at sowing):** NPK 60:30:30 kg/acre
- **Top dressing:** 30 kg N at 21 & 45 days after transplanting
- **Special:** Zinc sulfate 25 kg/acre at nursery

### Wheat:
- **At sowing:** NPK 80:40:40 kg/acre
- **Top dressing:** 40 kg N at first irrigation (crown root initiation)
- **Special:** Sulfur 20 kg/acre for light soils

### Maize:
- **At sowing:** NPK 80:40:40 kg/acre
- **Top dressing:** 40 kg N at knee high stage
- **Special:** Zinc sulfate 25 kg/acre

### Sugarcane:
- **At planting:** NPK 150:60:60 kg/acre
- **Split application:** 3 doses over growing period
- **Special:** FYM 10 tonnes/acre

## Organic Options:
- 🌱 Farmyard Manure (FYM) - 5-10 tonnes/acre
- 🌱 Vermicompost - 2-3 tonnes/acre  
- 🌱 Neem Cake - 250 kg/acre
- 🌱 Mustard Cake - 250 kg/acre
- 🌱 Bone Meal - 100 kg/acre

## Application Tips:
1. **Timing:** Apply at right growth stage
2. **Method:** Band placement better than broadcasting
3. **Water:** Ensure adequate moisture after application
4. **Balance:** Don't over-apply - more isn't always better!

Would you like specific recommendations for your crop and soil conditions?"""
    
    def _get_water_info(self, query, crop_type):
        """Irrigation and water management"""
        return f"""💧 **Water Management Guide**

## Critical Water Requirements by Crop:

### Rice:
- **Water need:** 1200-1500 mm per season
- **Method:** Puddling and continuous flooding
- **Critical stages:** Transplanting, tillering, flowering
- **Tips:** Maintain 2-5 cm water level, drain 15 days before harvest

### Wheat:
- **Water need:** 400-600 mm per season
- **Critical stages:** Crown root initiation, booting, grain filling
- **Irrigation schedule:**
  - 1st: 21-25 days after sowing
  - 2nd: 45-50 days (flowering)
  - 3rd: 70-75 days (grain filling)

### Maize:
- **Water need:** 500-800 mm per season
- **Critical stages:** Knee high, tasseling, grain filling
- **Avoid:** Water stress at pollination!

### Sugarcane:
- **Water need:** 1500-2500 mm per season
- **Method:** Drip irrigation saves 30-40% water
- **Frequency:** Weekly irrigation in summer

## Water-Saving Techniques:

### 🚿 Drip Irrigation:
- Saves 30-60% water
- Reduces weed growth
- Fertilizer application through water
- Initial cost high, long-term savings

### 🌾 Alternate Wetting and Drying (AWD):
- For rice: Allow water to recede to 5-15 cm before next irrigation
- Saves 20-30% water
- Reduces methane emissions

### 💦 Mulching:
- Plastic mulching: Saves 20-30% water
- Organic mulching: Improves soil health

### 🌧️ Rainwater Harvesting:
- Farm ponds
- Check dams
- Contour bunding
- Rooftop rainwater collection

## Drought Management:
1. Mulching to reduce evaporation
2. Anti-transpirant sprays
3. Drought-resistant varieties
4. Soil moisture conservation
5. Deficit irrigation scheduling

What specific water issue are you facing?"""
    
    def _get_climate_info(self, query, crop_type):
        """Climate and weather information"""
        return f"""🌡️ **Climate & Weather Management**

## Ideal Growing Conditions:

### Rice:
- Temperature: 20-35°C (optimal 25-30°C)
- Humidity: 70-90%
- Rainfall: 1500-2500 mm
- Sensitive to: Cold (<15°C), extreme heat (>40°C)

### Wheat:
- Temperature: 10-25°C (optimal 15-20°C)
- Cold requirement: 0-10°C for 6-8 weeks (vernalization)
- Sensitive to: Frost at flowering, heat at maturity

### Maize:
- Temperature: 18-35°C (optimal 25-30°C)
- Sensitive to: Frost, cold stress at seedling stage
- Heat tolerance: Good, but >40°C affects pollination

### Sugarcane:
- Temperature: 20-40°C (optimal 30-35°C)
- High sunshine requirement
- Sensitive to: Frost, prolonged cold

## Climate Change Adaptation:

### Heat Stress Management:
1. 🌳 Agroforestry - shade trees around fields
2. 💧 Mulching - cool soil surface
3. 🌾 Early morning/evening irrigation
4. 🌿 Anti-transpirants (kaolin, sunscreen)
5. 🧬 Heat-tolerant varieties

### Cold/Frost Protection:
1. 🌾 Smoke generation
2. 💧 Light irrigation before frost
3. 🌱 Mulching
4. 🏠 Poly-tunnels for sensitive crops
5. 🎯 Timely sowing to avoid frost period

### Extreme Weather Preparedness:

**Drought:**
- Drought-resistant varieties
- Water conservation techniques
- Crop insurance

**Flood:**
- Raised bed planting
- Drainage systems
- Flood-tolerant varieties
- Crop insurance

**Storms:**
- Windbreaks
- Support for tall crops
- Timely harvesting

## Seasonal Calendar:
- **Kharif (June-Oct):** Rice, Maize, Sugarcane, Cotton
- **Rabi (Nov-Mar):** Wheat, Chickpea, Mustard, Vegetables
- **Zaid (Mar-June):** Summer crops, vegetables

What climate-related challenge are you facing?"""
    
    def _get_soil_info(self, query, crop_type):
        """Soil health and management"""
        return f"""🧪 **Soil Health & Management**

## Understanding Soil pH:

| pH Range | Classification | Crops Suitable |
|----------|----------------|-----------------|
| < 5.0 | Strong Acid | Tea, Coffee, Blueberry |
| 5.0-6.0 | Moderate Acid | Rice, Wheat, Potato |
| 6.0-7.0 | Neutral | Most vegetables, maize |
| 7.0-8.0 | Alkaline | Cotton, Sugarbeet |
| > 8.0 | Strong Alkaline | Most crops struggle |

## pH Adjustment:

### For Acidic Soils (pH < 6.0):
- **Liming materials:**
  - Dolomite: 100-200 kg/acre
  - Lime: 100-150 kg/acre
  - Wood ash: 200-300 kg/acre
- Apply 3-4 months before planting

### For Alkaline Soils (pH > 8.0):
- **Gypsum:** 200-400 kg/acre
- **Sulfur:** 20-40 kg/acre
- **Organic matter:** FYM, compost
- **Mulching:** Helps acidify over time

## Improving Soil Health:

### Physical Properties:
1. **Organic Matter:** 2-3% ideal
   - Add FYM, compost, vermicompost
   - Crop residues incorporation
   - Green manuring

2. **Soil Structure:**
   - Avoid over-tillage
   - Use cover crops
   - Reduced tillage practices
   - Avoid working when wet

### Chemical Properties:
1. **Regular soil testing** - Every 2-3 years
2. **Balanced fertilization** - Based on test results
3. **Micronutrients** - Often deficient
   - Zinc: Common in alkaline soils
   - Iron: Common in high pH
   - Boron: Deficient in light soils

### Biological Properties:
1. **Beneficial microbes:**
   - Rhizobium for legumes
   - Azotobacter, Azospirillum
   - Trichoderma
   - PSM (Phosphorus Solubilizing Bacteria)

2. **Earthworm activity** - Indicator of soil health

## Cover Crops & Green Manuring:
- Dhaincha (Sesbania)
- Cowpea
- Sunhemp
- Mustard (must be incorporated before seeding)

## Soil Testing Recommendations:
- Test every 2-3 years
- Sample from 0-15 cm depth
- Collect 15-20 samples per field
- Mix and take composite sample

Would you like specific advice for your soil type?"""
    
    def _get_yield_info(self, query, crop_type):
        """Yield optimization strategies"""
        return f"""📈 **Yield Optimization Guide**

## Factors Affecting Yield:

### 1. Genetic Potential
- Choose right variety for your region
- Use certified quality seeds
- Hybrid vs. OP varieties

### 2. Environment
- Climate suitability
- Soil type and health
- Water availability

### 3. Management Practices
- Planting density
- Nutrient management
- Pest and disease control
- Harvest timing

## Yield Potential by Crop:

### Rice:
- **Traditional:** 2-3 tonnes/acre
- **Improved:** 4-6 tonnes/acre  
- **Hybrid:** 6-8 tonnes/acre
- **SRI Method:** 6-10 tonnes/acre

### Wheat:
- **Traditional:** 1.5-2 tonnes/acre
- **Improved:** 2.5-3.5 tonnes/acre
- **Hybrid:** 3.5-4.5 tonnes/acre

### Maize:
- **Traditional:** 2-3 tonnes/acre
- **Improved:** 3-4 tonnes/acre
- **Hybrid:** 4-6 tonnes/acre

### Sugarcane:
- **Traditional:** 30-40 tonnes/acre
- **Improved:** 40-50 tonnes/acre
- **High-yielding:** 50-70 tonnes/acre

## Key Strategies to Increase Yield:

### 🌱 Quality Seeds:
- Buy certified seeds
- Treat seeds before sowing
- Right seed rate

### 📏 Plant Density:
- Proper spacing is crucial
- Too close = competition
- Too far = wastage of area

### 💧 Water Management:
- Critical stage irrigation
- Avoid water stress
- Drainage as important as irrigation

### 🧪 Nutrient Management:
- Soil test based
- Split application
- Foliar feeding for micronutrients
- Organic supplements

### 🦠 Integrated Pest Management:
- Regular scouting
- Economic threshold levels
- Biological control first
- Chemical as last resort

### 🏆 Advanced Techniques:
- SRI (System of Rice Intensification)
- Drip irrigation with fertigation
- Precision agriculture
- Drone-based monitoring

## Profit Optimization:
1. **Reduce input costs** - Efficient resource use
2. **Quality produce** - Better market price
3. **Direct marketing** - Skip middlemen
4. **Value addition** - Processing
5. **Crop insurance** - Risk management

What specific yield challenges are you facing?"""
    
    def _get_planting_info(self, query, crop_type):
        """Planting and cultivation information"""
        return f"""🌱 **Planting & Cultivation Guide**

## Seed Selection:

### Quality Seeds Characteristics:
✅ High germination rate (>85%)
✅ Physical purity (>98%)
✅ Moisture content (<12%)
✅ Free from disease
✅ Proper seed size

### Seed Treatment:
1. ** Fungicide treatment:**
   - Carbendazim 2g/kg seed
   - Thiram 2g/kg seed

2. **Bio-control agents:**
   - Trichoderma 5g/kg seed
   - Pseudomonas 5g/kg seed

3. **Nutrient treatment:**
   - Azospirillum 5g/kg seed (for cereals)
   - Rhizobium 5g/kg seed (for legumes)

## Sowing Time:

### Kharif Season (Monsoon):
- **Rice:** June-July (nursery: May-June)
- **Maize:** June-July
- **Sugarcane:** Feb-March (spring) or Oct-Nov (autumn)

### Rabi Season (Winter):
- **Wheat:** October-November
- **Chickpea:** October-November
- **Mustard:** October

## Sowing Methods:

### 1. Direct Sowing:
- Broadcasting
- Drilling
- Line sowing

### 2. Transplanting:
- Rice seedling transplanting
- Vegetable seedlings

### 3. Modern Methods:
- **DAPRA Planting:** Uniform spacing, better growth
- **Precision Seeding:** Single seed per hill
- **SRI Method:** Wider spacing, individual plants

## Spacing Guidelines:

### Rice:
- **Transplanted:** 20x15 cm or 25x25 cm
- **Direct seeded:** 20-25 cm between rows

### Wheat:
- **Broadcasting:** 100 kg/acre
- **Line sowing:** 20-22.5 cm between rows

### Maize:
- **Single crop:** 60x30 cm
- **Intercrop:** 120x30 cm

## Depth of Sowing:
- **Small seeds (wheat, rice):** 2-3 cm
- **Medium seeds (maize):** 4-5 cm
- **Large seeds (pulses):** 5-7 cm

## Tips for Successful Sowing:
1. ✅ Prepare fine seedbed
2. ✅ Ensure adequate moisture
3. ✅ Sow at optimal depth
4. ✅ Cover seeds properly
5. ✅ Protect from birds/insects
6. ✅ Avoid sowing in extreme weather

Would you like guidance for a specific crop?"""
    
    def _get_general_farming_info(self, query, crop_type):
        """General farming advice"""
        return f"""🌾 **Welcome to AgriGuard AI - Comprehensive Farming Assistance**

I'm here to help you with all aspects of agriculture. Here are some topics I can assist you with:

---

### 🌱 **Crop Management**
- Variety selection
- Planting schedules
- Growth monitoring
- Harvesting techniques

### 🦠 **Disease & Pest Management**
- Disease identification
- Treatment options
- Organic solutions
- Prevention strategies

### 💧 **Water Management**
- Irrigation scheduling
- Water-saving techniques
- Drought management
- Flood protection

### 🧪 **Nutrient Management**
- Fertilizer recommendations
- Organic farming
- Soil health
- Composting

### 🌡️ **Climate Adaptation**
- Weather management
- Seasonal planning
- Climate-resilient farming

### 📊 **Economics**
- Cost reduction
- Government schemes
- Market information
- Profit optimization

---

## How to Get Best Advice:

Please tell me:
1. **What crop** are you growing?
2. **What is the issue?** (disease, pest, nutrient deficiency, etc.)
3. **What are the symptoms?** (describe what you see)
4. **Your location/climate** (for regional advice)

I provide detailed, actionable advice similar to agricultural experts. Ask me anything!"""
    
    def analyze_image(self, image_filename):
        """
        Simulate AI image analysis for disease detection
        In production, this would use a trained ML model
        """
        import random
        
        # Simulated analysis - in real app, use TensorFlow/PyTorch model
        diseases_detected = [
            {
                "disease": "Leaf Blight",
                "confidence": 87,
                "affected_area": "15%",
                "severity": "Moderate",
                "description": "Fungal infection detected on leaf margins. Common in humid conditions.",
                "treatment": {
                    "chemical": "Apply Mancozeb 75% WP @ 2.5g/L or Propiconazole 25% EC @ 1ml/L",
                    "organic": "Neem oil spray 5ml/L, remove affected leaves, improve air circulation",
                    "prevention": "Avoid overhead irrigation, use resistant varieties, maintain field sanitation"
                },
                "recovery_time": "7-14 days with treatment"
            },
            {
                "disease": "Nutrient Deficiency (Nitrogen)",
                "confidence": 92,
                "affected_area": "30%",
                "severity": "Moderate",
                "description": "Yellowing of older leaves indicates nitrogen deficiency. Common in early growth stages.",
                "treatment": {
                    "chemical": "Apply Urea 46% @ 2-3 kg/acre as top dressing",
                    "organic": "Apply FYM 5-10 tonnes/acre or Neem cake 250 kg/acre",
                    "prevention": "Regular soil testing, balanced fertilization, use of slow-release fertilizers"
                },
                "recovery_time": "10-21 days with treatment"
            },
            {
                "disease": "Bacterial Spot",
                "confidence": 78,
                "affected_area": "8%",
                "severity": "Mild",
                "description": "Small water-soaked lesions that turn brown. Spreads through rain splash.",
                "treatment": {
                    "chemical": "Apply Copper Oxychloride 50% WP @ 2.5g/L",
                    "organic": "Remove infected plant parts, improve drainage, avoid working in wet fields",
                    "prevention": "Use disease-free seeds, crop rotation, avoid overhead irrigation"
                },
                "recovery_time": "7-10 days with treatment"
            },
            {
                "disease": "Healthy - No Disease Detected",
                "confidence": 95,
                "affected_area": "0%",
                "severity": "None",
                "description": "Plant appears healthy with good green coloration and no visible disease symptoms.",
                "treatment": {
                    "chemical": "No treatment needed",
                    "organic": "Continue current practices, maintain balanced nutrition",
                    "prevention": "Continue preventive measures, monitor regularly"
                },
                "recovery_time": "N/A - Plant is healthy"
            }
        ]
        
        # Random selection for demo - in production, use actual ML prediction
        result = random.choice(diseases_detected)
        
        return {
            "status": "success",
            "analysis": result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "model_version": "AgriGuard AI v2.0",
            "recommendations": [
                "Isolate affected plants if possible",
                "Apply recommended treatment immediately",
                "Monitor nearby plants for similar symptoms",
                "Document the condition for future reference",
                "Consider soil testing if problem persists"
            ]
        }


# Initialize global assistant
farming_assistant = AIFarmingAssistant()
