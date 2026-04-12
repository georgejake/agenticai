import google.generativeai as genai
import os
from dotenv import load_dotenv
# Configure your API key
load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# List all models available to your key
for model in genai.list_models():
    print(model.name)