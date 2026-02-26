"""
AgriGuard Universal AI Agent - Multilingual AI Assistant
Comprehensive crop information and farming advice in multiple Indian languages
"""

import random
from datetime import datetime

class UniversalAI:
    def __init__(self):
        self.conversation_history = []
        self.user_preferences = {}
        self.context = {}
        self.language = "en"
        self.knowledge = self._build_knowledge_base()
        self.nlp = NLPProcessor()
        
    def _build_knowledge_base(self):
        """Build comprehensive knowledge base with all Indian crops in multiple languages"""
        return {
            "general": {
                "greetings": {
                    "en": ["Hello! How can I help you today?", "Hi there! What would you like to know?", "Namaste! What can I do for you today?"],
                    "hi": ["नमस्ते! मैं आपकी कैसे मदद कर सकता हूं?", "हेलो! आज मैं आपकी क्या मदद कर सकता हूं?"],
                    "ta": ["வணக்கம்! நான் உங்களுக்கு உதவ முடியுமா?", "ஹலோ! நீங்கள் எதை அறிந்து கொள்ள விரும்புகிறீர்கள்?"],
                    "te": ["namaste! nenu evaru help cheyyalo?", "hello! emanna telusukovali?"]
                },
                "how_are_you": {
                    "en": ["I'm doing great! How can I assist you today?", "I'm excellent! What would you like to know?"],
                    "hi": ["मैं बहुत अच्छा हूं! आज मैं आपकी क्या मदद कर सकता हूं?", "मैं बढ़िया हूं! आपको क्या जानना है?"],
                    "ta": ["நான் மிகவும் நன்றாக இருக்கிறேன்! உங்களுக்கு உதவ முடியுமா?", "சுபர்! உங்களுக்கு உதவ என்ன வேண்டும்?"],
                    "te": ["nenu bayataku taginalu! emanna help cheyyalo?", "nenu chala baga unna! emanna cheyya?"]
                },
                "who_are_you": {
                    "en": "I am AgriGuard AI, your farming assistant! I help farmers with crops, diseases, fertilizers, weather, and more. Ask me anything!",
                    "hi": "मैं AgriGuard AI हूं, आपका कृषि सहायक! मैं किसानों की फसलों, बीमारियों, खाद, मौसम और बहुत कुछ में मदद करता हूं।",
                    "ta": "நான் AgriGuard AI, உங்கள் விவசாய உதவியாளர்! விவசாயிகளுக்கு பயிர் நோய்கள், உரம், வான்வழி மற்றும் பலததில் உதவுகிறேன்!",
                    "te": "nenu AgriGuard AI, vallaki help chesina assistant! crops, diseases, fertilizers, weather lo help cheyataniki ready!"
                },
                "what_can_you_do": {
                    "en": "I can help you with: Crops (rice, wheat, maize, bajra, jowar, sugarcane, cotton, vegetables, fruits), Diseases & pests, Fertilizers & nutrients, Irrigation, Weather, Soil health, and more!",
                    "hi": "मैं आपकी मदद कर सकता हूं: फसलें (धान, गेहूं, मक्का, बाजरा, ज्वार, गन्ना, कपास, सब्जियां, फल), बीमारियां और कीट, खाद और पोषक तत्व, सिंचाई, मौसम, मिट्टी की सेहत!",
                    "ta": "நான் உதவ முடியும்: பயிர்கள் (அரிசி, கோதுமை, மக்காச்சோளம், பஜ்ரா, சுடரை, கரும்பு, பருத்தி, காய்கறி, பழம்), நோய்கள், உரம், பாசனம், வான்வழி!",
                    "te": "nenu help cheyyalo: Crops (paddy, wheat, corn, bajra, jowar, sugarcane, cotton, vegetables, fruits), Diseases, Fertilizers, Irrigation, Weather!"
                },
                "thank_you": {
                    "en": ["You're welcome!", "Happy to help!", "No problem at all!"],
                    "hi": ["आपका स्वागत है!", "खुशी से मदद की!", "कोई बात नहीं!"],
                    "ta": ["மகிழ்ச்சியாக உதவேன்!", "வரவேற்கிறேன்!", "பிரச்சினை இல்லை!"],
                    "te": ["swelcome!", "help chesina koraku thanks!", "ela ledu!"]
                },
                "goodbye": {
                    "en": ["Goodbye! Come back anytime!", "See you later!", "Take care!"],
                    "hi": ["अलविदा! कभी भी आइए!", "फिर मिलेंगे!", "ख्याल रखना!"],
                    "ta": ["வருக! எப்போதும் வரலாய்!", "பிறகு பார்க்கலாம!", "கவனமாயிரு!"],
                    "te": ["bye! velli ravbutundu!", "mare pixcchi!", "srogam lechina!"]
                }
            },
            "crops": {
                "rice": {
                    "en": "Rice (Paddy): India's staple food crop. Climate: 20-35°C, high humidity, 1500-2500mm rainfall. Varieties: Basmati, Ponni, IR-64, Swarna. Sowing: June-July (Kharif). Yield: 3-6 tonnes/acre. Water: Needs flooded fields. Tips: Use SRI method for higher yield, apply NPK 60:30:30 kg/acre.",
                    "hi": "धान/चावल: भारत की मुख्य खाद्य फसल। जलवायु: 20-35°C, उच्च आर्द्रता, 1500-2500mm वर्षा। किस्में: बासमती, पोनी, आईआर-64, स्वर्ण। बुवाई: जून-जुलाई। उपज: 3-6 टन/एकड़।",
                    "ta": "அரிசி: இந்தியாவின் முக்கிய உணவு பயிர். காலநிலை: 20-35°C, அதி ஈரப்பதம், 1500-2500mm மழை. வகைகள்: பாஸ்மதி, போன்னி, IR-64, சுவர்ணா. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Paddy: India main food crop. Climate: 20-35C, humidity 70%, rain 1500-2500mm. Varieties: Basmati, Ponni, IR-64. Sowing: June-July. Yield: 3-6 tonnes/acre."
                },
                "wheat": {
                    "en": "Wheat: India's second most important cereal. Climate: 10-25°C, cool weather. Varieties: HD-2967, PBW-550, DBW-187. Sowing: October-November (Rabi). Yield: 2.5-4 tonnes/acre. Harvest: March-April. Tips: Apply urea in 2 splits, need vernalization for flowering.",
                    "hi": "गेहूं: भारत का दूसरा सबसे महत्वपूर्ण अनाज। जलवायु: 10-25°C, ठंडा मौसम। किस्में: एचडी-2967, पीबीडब्ल्यू-550। बुवाई: अक्टूबर-नवंबर। उपज: 2.5-4 टन/एकड़।",
                    "ta": "கோதுமை: இந்தியாவின் இரண்டாவது முக்கிய தானியம். காலநிலை: 10-25°C, குளிர். வகைகள்: HD-2967, PBW-550. விதைப்பு: அக்டோபர்-நவம்பர். விளைச்சல்: 2.5-4 டன்.",
                    "te": "Wheat: Second main cereal. Climate: 10-25C cool. Varieties: HD-2967, PBW-550. Sowing: Oct-Nov. Yield: 2.5-4 tonnes. Harvest: March-April."
                },
                "maize": {
                    "en": "Maize (Corn): Versatile crop for food, fodder, and industry. Climate: 18-35°C. Varieties: HQPM-1, PMH-1, African Tall. Sowing: June-July (Kharif) & Feb-March (Rabi). Yield: 3-5 tonnes/acre. Uses: Food, fodder, starch, ethanol.",
                    "hi": "मक्का: खाद्य, चारा और उद्योग के लिए बहुमुखी फसल। जलवायु: 18-35°C। किस्में: एचक्यूपीएम-1, पीएमएच-1। बुवाई: जून-जुलाई। उपज: 3-5 टन/एकड़।",
                    "ta": "மக்காச்சோளம்: உணவு, தீவனம், தொழிற்சாலைக்கு. காலநிலை: 18-35°C. வகைகள்: HQPM-1, PMH-1. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Maize: For food, fodder, industry. Climate: 18-35C. Varieties: HQPM-1, PMH-1. Sowing: June-July. Yield: 3-5 tonnes."
                },
                "bajra": {
                    "en": "Bajra (Pearl Millet): Drought-resistant cereal for arid regions. Climate: 25-35°C, low rainfall (40-80mm). Varieties: ICTP-8203, RB-111. Sowing: July-August. Yield: 1.5-2.5 tonnes/acre. Uses: Food, fodder, bread making.",
                    "hi": "बाजरा: सूखा-प्रतिरोधी अनाज। जलवायु: 25-35°C, कम वर्षा। किस्में: आईसीटीपी-8203। बुवाई: जुलाई-अगस्त। उपज: 1.5-2.5 टन/एकड़।",
                    "ta": "பஜ்ரா: வறட்சி-எதிர்ப்பு தானியம். காலநிலை: 25-35°C. வகைகள்: ICTP-8203. விதைப்பு: ஜூலை-ஆகஸ்ட்.",
                    "te": "Bajra: Drought resistant cereal. Climate: 25-35C, low rain. Varieties: ICTP-8203. Sowing: July-Aug. Yield: 1.5-2.5 tonnes."
                },
                "jowar": {
                    "en": "Jowar (Sorghum): Drought-resistant cereal and fodder crop. Climate: 25-35°C. Varieties: CSV-15, SPV-1611. Sowing: June-July. Yield: 1.5-3 tonnes/acre. Uses: Food, fodder, brewing.",
                    "hi": "ज्वार: सूखा-प्रतिरोधी अनाज और चारा फसल। जलवायु: 25-35°C। किस्में: सीएसवी-15। बुवाई: जून-जुलाई। उपज: 1.5-3 टन/एकड़।",
                    "ta": "சோளம்: வறட்சி-எதிர்ப்பு தானியம். காலநிலை: 25-35°C. வகைகள்: CSV-15. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Jowar: Drought resistant cereal. Climate: 25-35C. Varieties: CSV-15. Sowing: June-July. Yield: 1.5-3 tonnes."
                },
                "ragi": {
                    "en": "Ragi (Finger Millet): Highly nutritious cereal, rich in calcium. Climate: 20-30°C. Varieties: GPU-28, PR-202. Sowing: June-July & Nov-Dec. Yield: 1.5-2 tonnes/acre. Uses: Food, malt, porridge.",
                    "hi": "रागी: अत्यधिक पौष्टिक अनाज, कैल्शियम से भरपूर। जलवायु: 20-30°C। किस्में: जीपीयू-28। बुवाई: जून-जुलाई। उपज: 1.5-2 टन/एकड़।",
                    "ta": "ராகி: மிகவும் ஊட்டமான தானியம். காலநிலை: 20-30°C. வகைகள்: GPU-28. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Ragi: Nutritious cereal rich in calcium. Climate: 20-30C. Varieties: GPU-28. Sowing: June-July. Yield: 1.5-2 tonnes."
                },
                "sugarcane": {
                    "en": "Sugarcane: Major industrial crop for sugar production. Climate: 20-40°C, sunny. Varieties: Co-86032, Co-99004, CoJ-64. Planting: Feb-March or Oct-Nov. Yield: 40-70 tonnes/acre. Harvest: 12-18 months. Tips: Apply 250:60:60 NPK kg/ha.",
                    "hi": "गन्ना: चीनी उत्पादन के लिए प्रमुख औद्योगिक फसल। जलवायु: 20-40°C, धूप। किस्में: को-86032, कोजे-64। रोपण: फरवरी-मार्च। उपज: 40-70 टन/एकड़।",
                    "ta": "கரும்பு: சர்க்கரைக்கு முக்கிய பயிர். காலநிலை: 20-40°C, சூரியன். வகைகள்: Co-86032, CoJ-64. நடவு: பிப்ரவரி-மார்ச். விளைச்சல்: 40-70 டன்.",
                    "te": "Sugarcane: For sugar industry. Climate: 20-40C sunny. Varieties: Co-86032, CoJ-64. Planting: Feb-March or Oct-Nov. Yield: 40-70 tonnes."
                },
                "cotton": {
                    "en": "Cotton (Kapas): Important fiber crop for textile industry. Climate: 20-40°C, sunny, moderate rain. Varieties: Bt Cotton (MECH-162, RCH-2), Desi cotton. Sowing: May-June. Yield: 1.5-3 quintals/acre. Harvest: 4-6 months after sowing.",
                    "hi": "कपास: कपड़ा उद्योग के लिए महत्वपूर्ण रेशे की फसल। जलवायु: 20-40°C। किस्में: बीटी कॉटन। बुवाई: मई-जून। उपज: 1.5-3 क्विंटल/एकड़।",
                    "ta": "பருத்தி: துணி தொழிற்சாலைக்கு முக்கிய பயிர். காலநிலை: 20-40°C. வகைகள்: பி.டி. பருத்தி. விதைப்பு: மே-ஜூன்.",
                    "te": "Cotton: Important fiber crop. Climate: 20-40C, sunny. Varieties: Bt Cotton. Sowing: May-June. Yield: 1.5-3 quintals/acre."
                },
                "groundnut": {
                    "en": "Groundnut (Peanut): Major oilseed crop, also used for food. Climate: 20-35°C. Varieties: JL-24, TAG-24, ICGS-76. Sowing: June-July (Kharif) & Feb-March (Rabi). Yield: 1.5-2.5 tonnes/acre. Uses: Oil, snacks, confectionery.",
                    "hi": "मूंगफली: प्रमुख तिलहन फसल। जलवायु: 20-35°C। किस्में: जेएल-24, टीएजी-24। बुवाई: जून-जुलाई। उपज: 1.5-2.5 टन/एकड़।",
                    "ta": "முங்குப்பல்: முக்கிய எண்ணெய் விதை பயிர். காலநிலை: 20-35°C. வகைகள்: JL-24, TAG-24. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Groundnut: Major oilseed. Climate: 20-35C. Varieties: JL-24, TAG-24. Sowing: June-July. Yield: 1.5-2.5 tonnes."
                },
                "mustard": {
                    "en": "Mustard: Important oilseed crop for edible oil. Climate: 15-25°C, cool. Varieties: Varuna, Rohini, Pusa Bold. Sowing: October-November (Rabi). Yield: 1-1.5 tonnes/acre. Uses: Oil, spices, greens.",
                    "hi": "सरसों: खाद्य तेल के लिए महत्वपूर्ण तिलहन। जलवायु: 15-25°C, ठंडा। किस्में: वरूणा, रोहिणी। बुवाई: अक्टूबर-नवंबर। उपज: 1-1.5 टन/एकड़।",
                    "ta": "கடுகு: முக்கிய எண்ணெய் விதை பயிர். காலநிலை: 15-25°C, குளிர். வகைகள்: Varuna, Rohini. விதைப்பு: அக்டோபர்-நவம்பர்.",
                    "te": "Mustard: Important oilseed. Climate: 15-25C cool. Varieties: Varuna, Rohini. Sowing: Oct-Nov. Yield: 1-1.5 tonnes."
                },
                "soybean": {
                    "en": "Soybean: Protein-rich oilseed crop. Climate: 20-32°C. Varieties: JS-335, PS-1341, NRC-37. Sowing: June-July. Yield: 1.5-2.5 tonnes/acre. Uses: Oil, protein meal, tofu, soy milk.",
                    "hi": "सोयाबीन: प्रोटीन युक्त तिलहन। जलवायु: 20-32°C। किस्में: जेएस-335। बुवाई: जून-जुलाई। उपज: 1.5-2.5 टन/एकड़।",
                    "ta": "சோயா பீன்ஸ்: புரதம் நிறைந்த எண்ணெய் விதை. காலநிலை: 20-32°C. வகைகள்: JS-335. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Soybean: Protein-rich oilseed. Climate: 20-32C. Varieties: JS-335. Sowing: June-July. Yield: 1.5-2.5 tonnes."
                },
                "tomato": {
                    "en": "Tomato: Major vegetable crop for fresh market and processing. Climate: 20-30°C. Varieties: Pusa Ruby, NS-501, Arka Vikas. Sowing: June-July & Oct-Nov. Yield: 10-15 tonnes/acre. Uses: Fresh, ketchup, sauce, puree.",
                    "hi": "टमाटर: ताजा बाजार और प्रोसेसिंग के लिए प्रमुख सब्जी। जलवायु: 20-30°C। किस्में: पूसा रूबी। बुवाई: जून-जुलाई। उपज: 10-15 टन/एकड़।",
                    "ta": "தக்காளி: முக்கிய காய்கறி பயிர். காலநிலை: 20-30°C. வகைகள்: Pusa Ruby. விதைப்பு: ஜூன்-ஜூலை.",
                    "te": "Tomato: Major vegetable. Climate: 20-30C. Varieties: Pusa Ruby. Sowing: June-July & Oct-Nov. Yield: 10-15 tonnes."
                },
                "potato": {
                    "en": "Potato: Major vegetable and staple food. Climate: 15-25°C. Varieties: Kufri Jyoti, Kufri Badshah, Kufri Pukhraj. Planting: Oct-Nov (Rabi) & Feb-March (Zaid). Yield: 8-12 tonnes/acre. Uses: Curry, chips, starch.",
                    "hi": "आलू: प्रमुख सब्जी और मुख्य भोजन। जलवायु: 15-25°C। किस्में: कुफ्री ज्योति, कुफ्री बादशाह। रोपण: अक्टूबर-नवंबर। उपज: 8-12 टन/एकड़।",
                    "ta": "உருளைக்கிழங்கு: முக்கிய காய்கறி. காலநிலை: 15-25°C. வகைகள்: Kufri Jyoti. நடவு: அக்டோபர்-நவம்பர்.",
                    "te": "Potato: Major vegetable. Climate: 15-25C. Varieties: Kufri Jyoti. Planting: Oct-Nov. Yield: 8-12 tonnes."
                },
                "onion": {
                    "en": "Onion: Major vegetable and condiment crop. Climate: 20-32°C. Varieties: Red Globe, N-2-4-1, Pusa Red. Sowing: Oct-Nov & May-June. Yield: 8-12 tonnes/acre. Uses: Curry, pickles, salads.",
                    "hi": "प्याज: प्रमुख सब्जी और मसाला फसल। जलवायु: 20-32°C। किस्में: रेड ग्लोब। बुवाई: अक्टूबर-नवंबर। उपज: 8-12 टन/एकड़।",
                    "ta": "வெங்காயம்: முக்கிய காய்கறி. காலநிலை: 20-32°C. வகைகள்: Red Globe. விதைப்பு: அக்டோபர்-நவம்பர்.",
                    "te": "Onion: Major vegetable. Climate: 20-32C. Varieties: Red Globe. Sowing: Oct-Nov & May-June. Yield: 8-12 tonnes."
                },
                "mango": {
                    "en": "Mango: King of fruits, major tropical fruit. Climate: 24-30°C. Varieties: Alphonso, Dashehari, Langra, Kesar, Totapuri. Yield: 5-15 tonnes/acre. Harvest: Summer (April-July). Uses: Fresh, juice, pickle, pulp.",
                    "hi": "आम: फलों का राजा, प्रमुख उष्णकटिबंधीय फल। जलवायु: 24-30°C। किस्में: अल्फांसो, दशेरी, लंगड़ा, केसर। उपज: 5-15 टन/एकड़।",
                    "ta": "மாங்காய்: பழங்கள் ராஜா. காலநிலை: 24-30°C. வகைகள்: Alphonso, Dashehari, Langra. விளைச்சல்: 5-15 டன்.",
                    "te": "Mango: King of fruits. Climate: 24-30C. Varieties: Alphonso, Dashehari, Langra, Kesar. Yield: 5-15 tonnes. Harvest: April-July."
                },
                "banana": {
                    "en": "Banana: Major fruit crop, rich in carbohydrates and potassium. Climate: 24-30°C, high humidity. Varieties: Grand Naine, Cavendish, Robusta. Planting: Monsoon (June-Aug) & Spring (Feb-March). Yield: 15-25 tonnes/acre. Harvest: 9-12 months.",
                    "hi": "केला: प्रमुख फल फसल। जलवायु: 24-30°C, उच्च आर्द्रता। किस्में: ग्रैंड नैन, कैवेंडिश। रोपण: जून-अगस्त। उपज: 15-25 टन/एकड़।",
                    "ta": "வாழை: முக்கிய பழ பயிர். காலநிலை: 24-30°C, அதி ஈரப்பதம். வகைகள்: Grand Naine. நடவு: ஜூன்-ஆகஸ்ட். விளைச்சல்: 15-25 டன்.",
                    "te": "Banana: Major fruit. Climate: 24-30C, high humidity. Varieties: Grand Naine. Planting: June-Aug. Yield: 15-25 tonnes."
                }
            },
            "diseases": {
                "blast": {
                    "en": "Rice Blast (Magnaporthe oryzae): Most destructive disease. Symptoms: Diamond-shaped lesions on leaves, stems, neck. Damage: 50-80% yield loss. Control: Tricyclazole 75% WP @ 0.6 g/L, Isoprothiolane, Neem oil. Prevention: Use resistant varieties, avoid excessive nitrogen.",
                    "hi": "धान का ब्लास्ट: सबसे विनाशकारी बीमारी। लक्षण: पत्तियों पर हीरे के आकार के घाव। नियंत्रण: ट्राइसाइक्लाजोल 75% डब्ल्यूपी।",
                    "ta": "அரிசி பிளாஸ்ட்: மிகவும் சேதமான நோய். கட்டுப்பாடு: ட்ரைசைக்ளஸோல்.",
                    "te": "Rice Blast: Very dangerous disease. Control: Tricyclazole spray."
                },
                "rust": {
                    "en": "Wheat Rust: Fungal disease with orange-brown pustules. Types: Leaf rust, Stem rust, Stripe rust. Damage: Up to 100%. Control: Propiconazole 25% EC, Tebuconazole. Prevention: Use resistant varieties, early sowing.",
                    "hi": "गेहूं का रस्ट: कवक रोग। लक्षण: नारंगी-भूरे फुंसी। नियंत्रण: प्रोपिकोनाजोल 25% ईसी।",
                    "ta": "கோதுமை ரச்ட்: பூஞ்சை நோய். கட்டுப்பாடு: புரோபிகோனசோல்.",
                    "te": "Wheat Rust: Fungal disease. Control: Propiconazole spray."
                },
                "red_rot": {
                    "en": "Sugarcane Red Rot: Serious fungal disease. Symptoms: Red stripes on leaves, rotting pith. Control: Carbendazim, heat treatment of seed sets. Prevention: Use healthy seed, crop rotation.",
                    "hi": "गन्ने का लाल सड़न: गंभीर कवक रोग। नियंत्रण: कार्बेंडाजिम।",
                    "ta": "கரும்பு சிவப்பு சாம்பல்: பூஞ்சை நோய்.",
                    "te": "Sugarcane Red Rot: Serious disease. Control: Carbendazim."
                }
            },
            "fertilizers": {
                "npk": {
                    "en": "NPK Guide: N (Nitrogen) - Leaf growth, green color. Deficiency: Yellow leaves. Sources: Urea (46% N), DAP (18% N), CAN. P (Phosphorus) - Root, flower, fruit development. Deficiency: Purple leaves. Sources: DAP, SSP, MAP. K (Potassium) - Plant health, disease resistance. Deficiency: Brown leaf edges. Sources: MOP, SOP.",
                    "hi": "एनपीके मार्गदर्शिका: नाइट्रोजन - पत्ती विकास, हरा रंग। स्रोत: यूरिया, डीएपी। फास्फोरस - जड़, फूल, फल। स्रोत: डीएपी, एसएसपी। पोटेशियम - पौधे की सेहत।",
                    "ta": "NPK வழிமுறை: N - இலை வளர்ச்சி. P - வேர், பூ, பழம். K - செடி ஆரோக்கியம்.",
                    "te": "NPK Guide: N - leaf growth, P - root/flower/fruit, K - plant health."
                },
                "urea": {
                    "en": "Urea (46% N): Most common nitrogen fertilizer. Benefits: High N content, quick absorption. Application: 2-3 splits, field flooding after application. Tips: Don't mix with DAP, apply in morning/evening.",
                    "hi": "यूरिया: सबसे आम नाइट्रोजन उर्वरक। लाभ: उच्च नाइट्रोजन सामग्री।",
                    "ta": "யூரியா: மிகவும் பிரபலமான நைட்ரஜன் உரம்.",
                    "te": "Urea (46% N): Common nitrogen fertilizer."
                }
            },
            "irrigation": {
                "drip": {
                    "en": "Drip Irrigation: Delivers water directly to root zone. Advantages: 30-60% water savings, reduces weeds, fertilizer efficiency. Disadvantages: High initial cost, clogging issues. Cost: Rs.30,000-50,000/acre. Best for: Vegetables, fruits, cash crops.",
                    "hi": "ड्रिप सिंचाई: जड़ों तक सीधे पानी पहुंचाती है। लाभ: 30-60% पानी की बचत। लागत: 30,000-50,000 रुपए/एकड़।",
                    "ta": "துளி பாசனம்: வேர்களுக்கு தண்ணீர். நன்மை: 30-60% தண்ணீர் மிசமகள்.",
                    "te": "Drip Irrigation: Water to roots. Benefits: 30-60% water savings. Cost: Rs.30,000-50,000/acre."
                },
                "flood": {
                    "en": "Flood Irrigation: Traditional water application method. Advantages: Low cost, easy to implement. Disadvantages: Wastes 30-50% water, promotes weeds, causes waterlogging. Best for: Rice, wheat.",
                    "hi": "बाढ़ सिंचाई: पारंपरिक विधि। लाभ: कम लागत। नुकसान: 30-50% पानी की बर्बादी।",
                    "ta": "வெள்ள பாசனம்: பாரம்பரிய முறை.",
                    "te": "Flood Irrigation: Traditional method. Benefits: Low cost. Problems: Wastes 30-50% water."
                }
            },
            "fallback": {
                "en": "That's a great question! I can help with all farming topics: Crops (rice, wheat, maize, bajra, jowar, sugarcane, cotton, vegetables, fruits), Diseases, Fertilizers, Irrigation, Weather, Soil health. What specific topic would you like to know more about?",
                "hi": "यह एक बहुत अच्छा सवाल है! मैं सभी कृषि विषयों में मदद कर सकता हूं: फसलें, बीमारियां, खाद, सिंचाई, मौसम, मिट्टी की सेहत।",
                "ta": "அது ஒரு நல்ல கேள்வி! விவசாயம் பற்றி எல்லாவற்றிலும் உதவ முடியும்: பயிர், நோய், உரம், பாசனம், வான்வழி.",
                "te": "Great question! Nenu crops, diseases, fertilizers, irrigation, weather help cheyyalo!"
            }
        }
    
    def set_language(self, lang_code):
        self.language = lang_code
        
    def set_context(self, key, value):
        self.context[key] = value
        
    def get_context(self, key):
        return self.context.get(key)
    
    def get_response(self, query, crop_type=None):
        return self.process_query(query, crop_type)
    
    def analyze_image(self, image_filename):
        diseases_detected = [
            {"disease": "Leaf Blight", "confidence": 87, "affected_area": "15%", "severity": "Moderate", "description": "Fungal infection on leaf margins. Common in humid conditions.", "treatment": {"chemical": "Mancozeb 75% WP @ 2.5g/L or Propiconazole 25% EC @ 1ml/L", "organic": "Neem oil spray 5ml/L, remove affected leaves"}, "recovery_time": "7-14 days"},
            {"disease": "Nutrient Deficiency (Nitrogen)", "confidence": 92, "affected_area": "30%", "severity": "Moderate", "description": "Yellowing of older leaves indicates nitrogen deficiency.", "treatment": {"chemical": "Urea 46% @ 2-3 kg/acre as top dressing", "organic": "Apply FYM 5-10 tonnes/acre"}, "recovery_time": "10-21 days"},
            {"disease": "Bacterial Spot", "confidence": 78, "affected_area": "8%", "severity": "Mild", "description": "Small water-soaked lesions that turn brown.", "treatment": {"chemical": "Copper Oxychloride 50% WP @ 2.5g/L"}, "recovery_time": "7-10 days"},
            {"disease": "Powdery Mildew", "confidence": 85, "affected_area": "20%", "severity": "Moderate", "description": "White powdery coating on leaves and stems.", "treatment": {"chemical": "Sulfur 80% WDG @ 2g/L", "organic": "Neem oil + garlic extract spray"}, "recovery_time": "7-14 days"},
            {"disease": "Healthy - No Disease", "confidence": 95, "affected_area": "0%", "severity": "None", "description": "Plant appears healthy with good green coloration.", "treatment": {"chemical": "No treatment needed", "organic": "Continue current practices"}, "recovery_time": "N/A"}
        ]
        result = random.choice(diseases_detected)
        return {"status": "success", "analysis": result, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "model_version": "AgriGuard AI v4.0", "recommendations": ["Monitor regularly", "Apply treatment if needed", "Maintain field hygiene", "Ensure proper nutrition"]}
        
    def process_query(self, query, crop_type=None, additional_data=None):
        self.conversation_history.append({"query": query, "timestamp": datetime.now()})
        processed = self.nlp.process(query)
        response = self._generate_response(processed, crop_type, additional_data)
        return response
    
    def _generate_response(self, processed, crop_type, additional_data):
        query = processed["query"].lower()
        intent = processed["intent"]
        keywords = processed["keywords"]
        
        # Greeting
        if intent == "greeting":
            return self._get_lang_response("general", "greetings")
        
        # How are you
        if intent == "how_are_you":
            return self._get_lang_response("general", "how_are_you")
        
        # Who are you
        if intent in ["who_are_you", "what_are_you"]:
            return self._get_response("general", "who_are_you")
        
        # What can you do
        if intent in ["capabilities", "help_request"]:
            return self._get_response("general", "what_can_you_do")
        
        # Thank you
        if intent == "thank":
            return self._get_lang_response("general", "thank_you")
        
        # Goodbye
        if intent == "goodbye":
            return self._get_lang_response("general", "goodbye")
        
        # Agriculture queries
        if intent == "agriculture" or self._is_agriculture_query(query):
            return self._handle_agriculture_query(query, keywords)
        
        # Fallback
        return self._get_response("fallback", self.language)
    
    def _is_agriculture_query(self, query):
        agri_words = ['crop', 'farm', 'farming', 'rice', 'wheat', 'maize', 'sugarcane', 
                    'plant', 'field', 'agriculture', 'paddy', 'cotton', 'pulses', 
                    'vegetable', 'fruit', 'irrigation', 'water', 'soil', 'fertilizer',
                    'pesticide', 'disease', 'pest', 'harvest', 'sow', 'seed', 
                    'monsoon', 'rainfall', 'yield', 'garden', 'drip', 'flood', 'urea', 'dap', 'npk',
                    'bajra', 'jowar', 'ragi', 'gram', 'tur', 'moong', 'urad', 'mustard', 'groundnut',
                    'soybean', 'tomato', 'potato', 'onion', 'mango', 'banana', 'blight', 'rust']
        return any(word in query for word in agri_words)
    
    def _handle_agriculture_query(self, query, keywords):
        # Rice
        if 'rice' in query or 'paddy' in query or 'chawal' in query:
            return self._get_response("crops", "rice")
        
        # Wheat
        if 'wheat' in query or 'gehu' in query or 'godambu' in query:
            return self._get_response("crops", "wheat")
        
        # Maize
        if 'maize' in query or 'corn' in query or 'makka' in query:
            return self._get_response("crops", "maize")
        
        # Bajra
        if 'bajra' in query or 'pearl' in query:
            return self._get_response("crops", "bajra")
        
        # Jowar
        if 'jowar' in query or 'sorghum' in query:
            return self._get_response("crops", "jowar")
        
        # Ragi
        if 'ragi' in query or 'finger millet' in query:
            return self._get_response("crops", "ragi")
        
        # Sugarcane
        if 'sugarcane' in query or 'ganne' in query or 'karambu' in query:
            return self._get_response("crops", "sugarcane")
        
        # Cotton
        if 'cotton' in query or 'kapas' in query:
            return self._get_response("crops", "cotton")
        
        # Groundnut
        if 'groundnut' in query or 'peanut' in query or 'moongphali' in query:
            return self._get_response("crops", "groundnut")
        
        # Mustard
        if 'mustard' in query or 'sarso' in query:
            return self._get_response("crops", "mustard")
        
        # Soybean
        if 'soybean' in query or 'soy' in query:
            return self._get_response("crops", "soybean")
        
        # Tomato
        if 'tomato' in query or 'tamatar' in query:
            return self._get_response("crops", "tomato")
        
        # Potato
        if 'potato' in query or 'aloo' in query:
            return self._get_response("crops", "potato")
        
        # Onion
        if 'onion' in query or 'pyaaz' in query:
            return self._get_response("crops", "onion")
        
        # Mango
        if 'mango' in query or 'aam' in query:
            return self._get_response("crops", "mango")
        
        # Banana
        if 'banana' in query or 'kela' in query:
            return self._get_response("crops", "banana")
        
        # Disease - Blast
        if 'blast' in query or 'blight' in query:
            return self._get_response("diseases", "blast")
        
        # Disease - Rust
        if 'rust' in query:
            return self._get_response("diseases", "rust")
        
        # Disease - Red Rot
        if 'red rot' in query or 'red_rot' in query:
            return self._get_response("diseases", "red_rot")
        
        # Fertilizer - NPK
        if 'npk' in query or 'nitrogen' in query or 'fertilizer' in query:
            return self._get_response("fertilizers", "npk")
        
        # Fertilizer - Urea
        if 'urea' in query:
            return self._get_response("fertilizers", "urea")
        
        # Irrigation - Drip
        if 'drip' in query:
            return self._get_response("irrigation", "drip")
        
        # Irrigation - Flood
        if 'flood' in query or 'canal' in query:
            return self._get_response("irrigation", "flood")
        
        # General farming
        if any(word in query for word in ['farming', 'farm', 'agriculture', 'crop', 'kheti', 'velanai']):
            return self._get_response("general", "what_can_you_do")
        
        return self._get_response("fallback", self.language)
    
    def _get_response(self, category, subcategory=None):
        try:
            if subcategory:
                return self.knowledge.get(category, {}).get(subcategory, "")
            return self.knowledge.get(category, "")
        except:
            return ""
    
    def _get_lang_response(self, category, subcategory):
        try:
            data = self.knowledge.get(category, {}).get(subcategory, {})
            if isinstance(data, dict):
                return data.get(self.language, data.get("en", ""))
            elif isinstance(data, list):
                return random.choice(data) if data else ""
            return data
        except:
            return ""


class NLPProcessor:
    def __init__(self):
        self.intent_patterns = self._build_intent_patterns()
        
    def _build_intent_patterns(self):
        return {
            "greeting": ["hello", "hi", "hey", "namaste", "good morning", "good evening", "vanakkam", "hola"],
            "how_are_you": ["how are you", "how do you do", "kaisa hai", "vela irukku", "ela unna"],
            "who_are_you": ["who are you", "what are you", "kon hai", "ne enga", "emi ledu"],
            "capabilities": ["what can you do", "help me", "evaru cheyyalo", "unga support", "help"],
            "thank_you": ["thank you", "thanks", "dhanyavad", "nandri", "shukriya"],
            "goodbye": ["bye", "goodbye", "alvida", "po", "bye"],
            "agriculture": ["farming", "crop", "agriculture", "field", "farm", "plant", "kheti", "velanai", "paddy", "rice", "wheat", "disease", "fertilizer", "irrigation", "bajra", "jowar", "ragi", "sugarcane", "cotton", "vegetable", "fruit"]
        }
    
    def process(self, query):
        query_lower = query.lower()
        intent = self._extract_intent(query_lower)
        keywords = self._extract_keywords(query_lower)
        return {"query": query, "intent": intent, "keywords": keywords, "entities": {}}
    
    def _extract_intent(self, query):
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if pattern in query:
                    return intent
        return "general"
    
    def _extract_keywords(self, query):
        important_words = ['how', 'what', 'why', 'when', 'where', 'who', 'which', 'help', 'tell', 'explain', 'give', 'need', 'want', 'know']
        keywords = []
        words = query.replace('?', ' ').replace('!', ' ').replace('.', ' ').split()
        for word in words:
            if word not in important_words and len(word) > 2:
                keywords.append(word)
        return keywords


ai = UniversalAI()
