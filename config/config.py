import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Credentials
API_KEY = os.getenv("MEXC_API_KEY")
API_SECRET = os.getenv("MEXC_API_SECRET")

# Trading Config
TRADE_SYMBOL = "XRPUSDT"
TRADE_QUANTITY = 0.01
PAPER_TRADING = True  # Set to False for real trading

# Initial Virtual Balance for Paper Trading
START_BALANCE = 10000.0  # Simulated balance in USD

# Trading Frequency
CHECK_INTERVAL = 1  # ⏳ Check market every second

# Safety Settings
STOP_LOSS_PERCENT = 1.5  # 1.5% stop loss
TAKE_PROFIT_PERCENT = 3.0  # 3% take profit
COOLDOWN_PERIOD = 30  # 30-second cooldown between trades

# Enable Short Trading
ENABLE_SHORT_TRADING = True  # Set to False to disable short trading

