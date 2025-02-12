import pandas as pd
import ta

def calculate_rsi(data, period=14):
    """
    Calculate RSI using Heikin Ashi close prices.
    """
    try:
        df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})

        # Use Heikin Ashi close prices instead of standard close prices
        rsi = ta.momentum.RSIIndicator(df["close"], window=period).rsi()
        return rsi.iloc[-1]

    except Exception as e:
        print(f"❌ Error in calculate_rsi(): {e}")
        return -1  # Return -1 on failure
