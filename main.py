import os
import requests

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")

response = requests.post("https://id.twitch.tv/oauth2/token", params={
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
})

token_data = response.json()
print(token_data)