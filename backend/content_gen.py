import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_press_release(company, topic, supplementary_data):
    """Generates a press release using Groq's API via HTTP request."""
    
    url = "https://api.groq.com/openai/v1/chat/completions"  # Check actual Groq endpoint
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-r1-distill-llama-70b",  # Model name from Groq's API
        "messages": [
            {"role": "system", "content": f"Write a professional press release for {company} about {topic}. Supplementary info: {supplementary_data}."}
        ],
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

