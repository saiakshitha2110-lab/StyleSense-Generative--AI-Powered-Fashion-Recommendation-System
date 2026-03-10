import os
import requests
import base64
import json
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

class FashionEngine:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

    def _call_gemini(self, payload):
        if not self.api_key:
            return "API Key not configured. Please check your .env file."
        
        url = f"{self.base_url}?key={self.api_key}"
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response_json = response.json()
            
            if 'candidates' in response_json:
                return response_json['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"Error from API: {response_json.get('error', {}).get('message', 'Unknown error')}"
        except Exception as e:
            return f"Request failed: {str(e)}"

    def get_recommendations(self, preferences):
        prompt = f"""
        Act as a professional high-end fashion stylist. 
        Provide 3 detailed outfit recommendations based on these preferences:
        - Gender: {preferences.get('gender')}
        - Age Group: {preferences.get('age')}
        - Occasion: {preferences.get('occasion')}
        - Style Preference: {preferences.get('style')}
        - Budget: {preferences.get('budget')}
        
        For each outfit, include:
        1. Top/Outerwear
        2. Bottom
        3. Footwear
        4. Accessories
        5. Stylist's Tip on why this works.
        
        Format the output in clean markdown with bold headers.
        """
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        return self._call_gemini(payload)

    def analyze_image(self, image_path, query="What style is this and how can I improve it?"):
        if not os.path.exists(image_path):
            return "Image file not found."

        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        payload = {
            "contents": [{
                "parts": [
                    {"text": f"As a fashion expert, analyze this image. {query}"},
                    {"inline_data": {"mime_type": "image/png", "data": image_data}}
                ]
            }]
        }
        return self._call_gemini(payload)

    def get_trend_insights(self):
        prompt = "Provide 3 current global fashion trends for 2024/2025 with brief descriptions and how to wear them."
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        return self._call_gemini(payload)
