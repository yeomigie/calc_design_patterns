from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
env = os.getenv("ENV")
api_key = os.getenv("API_KEY")

print(f"Environment: {env}")
print(f"API Key: {api_key}")
