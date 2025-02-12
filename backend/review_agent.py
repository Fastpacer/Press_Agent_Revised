import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def clean_json_output(response_text):
    """Cleans AI response and extracts valid JSON data."""
    try:
        # Remove triple backticks if they exist
        response_text = response_text.strip().strip("```json").strip("```")
        
        # Convert cleaned text to JSON
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from AI", "raw_response": response_text}

def review_press_kit(text):
    """Uses Groq API to analyze the press kit quality."""
    
    url = "https://api.groq.com/openai/v1/chat/completions"  # Ensure this is the correct endpoint
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    Evaluate the following press kit based on:
    - Content Consistency (0-10)
    - Writing Style (0-10)
    - Layout and Structure (0-10)
    - SEO Optimization (0-10)
    Provide scores and constructive feedback in JSON format.

    Press Kit:
    {text}
    """
    
    payload = {
        "model": "deepseek-r1-distill-llama-70b",
        "messages": [{"role": "system", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        ai_response = response.json()["choices"][0]["message"]["content"]
        return clean_json_output(ai_response)  # Clean & parse JSON properly
    else:
        return {"error": f"API Error {response.status_code}", "message": response.text}
