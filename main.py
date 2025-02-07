import time
from trading.mexc_client import get_klines
from strategies.strategy import trade_logic
from trading.orders import place_order
from config.config import TRADE_SYMBOL, CHECK_INTERVAL

while True:
    try:
        data = get_klines(symbol=TRADE_SYMBOL)  # Fetch market data
        decision = trade_logic(data)
        last_close_price = float(data[-1][5])  # Latest close price

        if decision == "BUY":
            print("🚀 Placing a BUY order...")
            place_order("BUY", last_close_price)
        elif decision == "SELL":
            print("🔻 Placing a SELL order...")
            place_order("SELL", last_close_price)
        elif decision == "SHORT":
            print("📉 Opening a SHORT position...")
            place_order("SHORT", last_close_price)
        elif decision == "COVER":
            print("📈 Closing a SHORT position...")
            place_order("COVER", last_close_price)
        else:
            print("⚠️ No trade executed.")

        time.sleep(CHECK_INTERVAL)  # ✅ Check every 1 second
    except Exception as e:
        print(f"❌ Error in main loop: {e}")

