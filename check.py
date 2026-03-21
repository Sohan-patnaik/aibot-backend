import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

print("Loaded key:", os.getenv("GOOGLE_API_KEY"))