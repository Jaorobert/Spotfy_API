import os
import base64
import requests
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

TOKEN_URL = "https://accounts.spotify.com/api/token"

credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"

credentials_base64 = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {credentials_base64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

response = requests.post(
    TOKEN_URL,
    headers=headers,
    data=data
)

print("Status Code:", response.status_code)
print(response.json())