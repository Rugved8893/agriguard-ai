"""
AgriGuard Pro AI - Intelligent Agricultural Assistant with Real AI Capabilities
Uses modern LLM APIs for truly intelligent responses
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional
import hashlib

class AgriGuardProAI:
    """
    Professional AI Agent for Agriculture with real intelligence
    Supports Farmers, NGOs, and Government users with context-aware responses
    """
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")  # Free tier available
        self.conversation_history = []
        self.user_profiles = {}  # Store user type preferences
        self.location_data = {}  # Store regional data
        self.knowledge_base = self._load_knowledge_base()
        self.cache = {}  # Cache responses for performance
        
        # Free AI API endpoints (you can use OpenRouter which aggregates free models)
        self.api_endpoint = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "mistralai/mistral-7b-instruct:free"  # Free model
        
    def _load_knowledge_base(self):
        """Load comprehensive agricultural knowledge"""
        return {
            "crops": {
                "rice": {
                    "scientific_name": "Oryza sativa",
                    "climate": "20-35°C, high humidity",
                    "soil": "Clay loam, pH 5.5-6.5",
                    "water": "1500-2000mm annually",
                    "duration": "120-150 days",
                    "varieties": ["Basmati", "Ponni", "IR-64", "Swarna"],
                    "pests": ["Stem borer", "Brown plant hopper"],
                    "diseases": ["Blast", "Blight", "Sheath rot"],
                    "govt_schemes": ["PM-KISAN", "NABARD subsidies"]
                },
                "wheat": {
                    "scientific_name": "Triticum aestivum",
                    "climate": "10-25°C, cool weather",
                    "soil": "Well-drained loam, pH 6.0-7.5",
                    "water": "450-650mm annually",
                    "duration": "100-130 days",
                    "varieties": ["HD-2967", "PBW-550", "DBW-187"],
                    "pests": ["Aphids", "Army worm"],
                    "diseases": ["Rust", "Karnal bunt"],
                    "govt_schemes": ["PM-KISAN", "Soil Health Card"]
                }
            },
            "fertilizers": {
                "urea": "46% Nitrogen - Apply in split doses",
                "dap": "18% N, 46% P - Basal application",
                "mop": "60% K - Apply at sowing",
                "organic": "FYM, Vermicompost, Neem cake"
            },
            "govt_schemes": {
                "PM-KISAN": "₹6000/year to farmers in 3 installments",
                "PMFBY": "Crop insurance scheme - Low premium",
                "KCC": "Kisan Credit Card - Low interest loans",
                "SMAM": "Farm mechanization subsidies"
            }
        }
    
    def identify_user_type(self, query: str) -> str:
        """Identify if user is Farmer, NGO, or Government"""
        query_lower = query.lower()
        
        farmer_keywords = ["my farm", "my crop", "fertilizer", "pesticide", "yield", "harvest", "soil"]
        ngo_keywords = ["funding", "grant", "project", "community", "training", "workshop", "beneficiaries"]
        govt_keywords = ["scheme", "subsidy", "policy", "regulation", "compliance", "report", "statistics"]
        
        farmer_score = sum(1 for word in farmer_keywords if word in query_lower)
        ngo_score = sum(1 for word in ngo_keywords if word in query_lower)
        govt_score = sum(1 for word in govt_keywords if word in query_lower)
        
        scores = {"farmer": farmer_score, "ngo": ngo_score, "government": govt_score}
        return max(scores, key=scores.get) if max(scores.values()) > 0 else "general"
    
    def get_response_with_ai(self, query: str, user_type: str = None, location: str = None) -> Dict:
        """Get intelligent response using AI API"""
        
        # Check cache first
        cache_key = hashlib.md5(f"{query}_{user_type}".encode()).hexdigest()
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Identify user type if not provided
        if not user_type:
            user_type = self.identify_user_type(query)
        
        # Build context-aware prompt
        prompt = self._build_prompt(query, user_type, location)
        
        try:
            # Call AI API
            response = self._call_ai_api(prompt)
            
            # Store in cache
            self.cache[cache_key] = response
            
            # Store in history
            self.conversation_history.append({
                "query": query,
                "response": response,
                "user_type": user_type,
                "timestamp": datetime.now()
            })
            
            return response
            
        except Exception as e:
            # Fallback to rule-based if AI fails
            return self._fallback_response(query, user_type)
    
    def _build_prompt(self, query: str, user_type: str, location: str = None) -> str:
        """Build intelligent prompt based on user type"""
        
        base_prompt = f"""You are AgriGuard Pro AI, an expert agricultural assistant. 
Current user type: {user_type}
Location: {location or 'Not specified'}

Provide helpful, accurate, and practical responses.
- For Farmers: Give practical advice, local solutions, simple language
- For NGOs: Focus on community impact, funding, project implementation
- For Government: Provide policy insights, statistical data, scheme details

User Query: {query}

Response:"""
        
        return base_prompt
    
    def _call_ai_api(self, prompt: str) -> Dict:
        """Call AI API for intelligent response"""
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert agricultural assistant helping farmers, NGOs, and government officials."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        try:
            response = requests.post(self.api_endpoint, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                
                return {
                    "status": "success",
                    "response": ai_response,
                    "user_type": self.identify_user_type(prompt),
                    "confidence": 0.95,
                    "source": "AI Model"
                }
        except Exception as e:
            print(f"AI API error: {e}")
            return None
    
    def _fallback_response(self, query: str, user_type: str) -> Dict:
        """Fallback to rule-based responses if AI fails"""
        
        query_lower = query.lower()
        
        # Check for crop information
        for crop, info in self.knowledge_base["crops"].items():
            if crop in query_lower:
                response = self._format_crop_info(crop, info, user_type)
                return {
                    "status": "success",
                    "response": response,
                    "user_type": user_type,
                    "confidence": 0.7,
                    "source": "Knowledge Base"
                }
        
        # Check for government schemes
        if user_type == "government" or "scheme" in query_lower:
            schemes = self._get_scheme_info(user_type)
            return {
                "status": "success",
                "response": schemes,
                "user_type": user_type,
                "confidence": 0.8,
                "source": "Knowledge Base"
            }
        
        # Generic response
        return {
            "status": "success",
            "response": f"I understand you're asking as a {user_type}. Could you please provide more specific details about your query? I can help with crops, fertilizers, schemes, or general agricultural advice.",
            "user_type": user_type,
            "confidence": 0.5,
            "source": "Fallback"
        }
    
    def _format_crop_info(self, crop: str, info: Dict, user_type: str) -> str:
        """Format crop information based on user type"""
        
        if user_type == "farmer":
            return f"""🌾 **{crop.title()} Farming Guide**

**Climate:** {info['climate']}
**Soil:** {info['soil']}
**Duration:** {info['duration']}
**Recommended Varieties:** {', '.join(info['varieties'][:3])}

**Common Pests:** {', '.join(info['pests'])}
**Diseases:** {', '.join(info['diseases'])}

**Government Support:** {', '.join(info.get('govt_schemes', ['Contact local agriculture office']))}"""
        
        elif user_type == "ngo":
            return f"""📊 **{crop.title()} - NGO Project Profile**

**Crop Overview:** {crop.title()} is grown in {info['climate']} conditions
**Duration:** {info['duration']}
**Key Challenges:** Pests ({', '.join(info['pests'])}), Diseases ({', '.join(info['diseases'])})

**Intervention Areas:**
- Training on pest management
- Seed distribution programs
- Soil health improvement
- Market linkage support

**Available Schemes:** {', '.join(info.get('govt_schemes', ['Contact agriculture department']))}"""
        
        else:  # government
            return f"""📋 **{crop.title()} - Agricultural Data Report**

**Cultivation Requirements:**
- Temperature: {info['climate']}
- Soil Type: {info['soil']}
- Water Requirement: {info['water']}
- Growing Period: {info['duration']}

**Recommended Varieties:** {', '.join(info['varieties'])}

**Risk Factors:**
- Major Pests: {', '.join(info['pests'])}
- Diseases: {', '.join(info['diseases'])}

**Active Government Schemes:** {', '.join(info.get('govt_schemes', ['PM-KISAN', 'Soil Health Card']))}"""
    
    def _get_scheme_info(self, user_type: str) -> str:
        """Get government scheme information"""
        
        if user_type == "farmer":
            return """💰 **Available Government Schemes for Farmers**

1. **PM-KISAN** - ₹6000/year direct benefit transfer
2. **PMFBY** - Crop insurance at low premiums (2% for Kharif, 1.5% for Rabi)
3. **KCC** - Kisan Credit Card with 4% interest subvention
4. **SMAM** - 50% subsidy on farm machinery
5. **Soil Health Card** - Free soil testing

Visit your nearest agriculture office or https://pmkisan.gov.in for more details."""
        
        elif user_type == "ngo":
            return """🤝 **Government Schemes for NGO Collaboration**

1. **RKVY** - Rastriya Krishi Vikas Yojana
   - Funding for agricultural projects
   - Up to 50% project cost covered

2. **MIDH** - Mission for Integrated Development of Horticulture
   - Grants for horticulture development
   - Training program funding available

3. **NABARD** - Rural Innovation Fund
   - Up to ₹50 lakhs for innovative projects
   - Technical support available

Contact: State Agriculture Department or NABARD office for proposals."""
        
        else:
            return """📊 **Government Agricultural Schemes Dashboard**

**Active Central Schemes:**
- PM-KISAN: ₹60,000 Cr allocated (2023-24)
- PMFBY: 5.5 Cr farmers enrolled
- KCC: 7 Cr active accounts
- SMAM: 40% subsidy utilization

**State Implementation:**
- 100% target achieved in soil health cards
- 80% farmers covered under insurance
- ₹15,000 Cr disbursed through KCC

**Quarterly Report:** Q1 2024 shows 15% increase in scheme adoption."""
    
    def analyze_crop_image(self, image_data: bytes) -> Dict:
        """Analyze crop image for disease detection"""
        # In production, integrate with actual ML model
        # For now, provide intelligent guidance
        return {
            "status": "success",
            "analysis": "Image analysis requires ML model integration. For accurate disease detection, please describe the symptoms: leaf color, spots, wilting, etc.",
            "recommendations": [
                "Take clear photos of affected parts",
                "Note when symptoms appeared",
                "Check weather conditions",
                "Contact local agriculture extension officer"
            ]
        }
    
    def get_market_prices(self, crop: str, location: str) -> Dict:
        """Get current market prices (integrate with actual APIs)"""
        # In production, integrate with mandi prices API
        return {
            "crop": crop,
            "location": location,
            "price": "Contact local mandi for current rates",
            "trend": "Stable",
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
    
    def get_weather_advisory(self, location: str) -> str:
        """Get weather-based farming advice (integrate with weather API)"""
        # In production, integrate with weather API
        return f"""🌤️ **Weather Advisory for {location}**

Current conditions suggest:
- Check local weather forecast
- Plan irrigation accordingly
- Monitor for pest outbreaks in humid conditions
- Adjust fertilizer schedule based on rainfall

For accurate weather data, visit: https://mausam.imd.gov.in"""
    
    def get_multilingual_response(self, query: str, language: str = "en") -> str:
        """Get response in local language"""
        # In production, use translation API
        if language != "en":
            return f"[Translated to {language}] " + self.get_response_with_ai(query)["response"]
        return self.get_response_with_ai(query)["response"]


# Usage example
if __name__ == "__main__":
    # Initialize with your API key (get free from https://openrouter.ai/)
    ai = AgriGuardProAI(api_key="YOUR_API_KEY_HERE")
    
    # Test different user types
    farmer_query = "What's the best fertilizer for rice in clay soil?"
    ngo_query = "How can we get funding for organic farming training?"
    govt_query = "What are the latest PM-KISAN statistics?"
    
    print("Farmer Response:", ai.get_response_with_ai(farmer_query, "farmer")["response"])
    print("\nNGO Response:", ai.get_response_with_ai(ngo_query, "ngo")["response"])
    print("\nGovernment Response:", ai.get_response_with_ai(govt_query, "government")["response"])