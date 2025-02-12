import time
from trading.mexc_client import get_klines
from strategies.strategy import trade_logic
from trading.orders import place_order, virtual_balance, btc_holdings, short_position
from config.config import TRADE_SYMBOL, CHECK_INTERVAL

while True:
    try:
        # ✅ Fetch latest market data
        data = get_klines(symbol=TRADE_SYMBOL)
        if not data:
            continue  # Skip iteration if no data

        last_close_price = float(data[-1][4])  # Latest close price

        # ✅ Get trade decision
        decision = trade_logic(data)

        # ✅ Ensure decision is valid
        if decision not in ["BUY", "SELL", "SHORT", "COVER", "HOLD"]:
            raise ValueError(f"Unexpected trade_logic() return value: {decision}")

        # ✅ Execute trade
        if decision == "BUY":
            place_order("BUY", last_close_price)
        elif decision == "SELL":
            place_order("SELL", last_close_price)
        elif decision == "SHORT":
            place_order("SHORT", last_close_price)
        elif decision == "COVER":
            place_order("COVER", last_close_price)

        # ✅ Print Summary Every Second (No Processed Data Spam)
        print(f"📊 Net Worth: ${virtual_balance + (btc_holdings + short_position) * last_close_price:.2f} | Last Trade: {decision}")

        # ✅ Sleep before next check
        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print(f"❌ Error in main loop: {e}")

