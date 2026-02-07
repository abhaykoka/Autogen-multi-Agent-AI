import os
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('GOOGLE_API_KEY')
print(f"API Key present: {bool(api_key)}")
if api_key:
    print(f"API Key start: {api_key[:5]}...")

genai.configure(api_key=api_key)

async def test_genai():
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        response = await asyncio.to_thread(
            model.generate_content,
            'Hello, are you working?'
        )
        print("Response received:")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_genai())
