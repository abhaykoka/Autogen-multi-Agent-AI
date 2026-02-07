import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key loaded: {bool(api_key)}")
if api_key:
    print(f"Key starts with: {api_key[:10]}...")

# Configure Gemini
genai.configure(api_key=api_key)

# Test with Gemini 2.0
try:
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content('Say "Hello, I am working!" if you can read this.')
    print("\n✓ Gemini 2.0 Flash Response:")
    print(response.text)
    print("\n✓ API connection successful!")
except Exception as e:
    print(f"\n✗ Error: {e}")
