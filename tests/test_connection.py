from mexc_sdk import Spot
from config.config import API_KEY, API_SECRET

# Initialize the MEXC client
client = Spot(api_key=API_KEY, api_secret=API_SECRET)

try:
    # Use the correct method name
    account_info = client.account_info()
    print("✅ Connection successful! Here is your account information:")
    print(account_info)
except Exception as e:
    print("❌ Connection failed. Error:", e)

