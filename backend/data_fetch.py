import requests
import os
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def fetch_supplementary_data(company):
    """Fetches latest market trends for the company using Tavily API."""
    url = f"https://api.tavily.com/search?q={company}&api_key={TAVILY_API_KEY}"
    response = requests.get(url)
    return response.json().get("results", []) if response.status_code == 200 else []
