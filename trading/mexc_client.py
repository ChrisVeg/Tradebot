import pandas as pd
from mexc_sdk import Spot
from config.config import API_KEY, API_SECRET

# Initialize MEXC Spot client
client = Spot(api_key=API_KEY, api_secret=API_SECRET)

def get_klines(symbol, interval="1m", limit=50):
    """
    Fetch Kline (candlestick) data and convert to Heikin Ashi candles.
    """
    raw_data = client.klines(symbol=symbol, interval=interval, options={"limit": limit})

    if not raw_data or len(raw_data) == 0:
        print("❌ Error: No data received from MEXC API")
        return []

    # ✅ Extract only the first 6 columns
    processed_data = [row[:6] for row in raw_data]

    # Convert to DataFrame
    df = pd.DataFrame(processed_data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})

    # Convert to Heikin Ashi Candles
    ha_df = convert_to_heikin_ashi(df)

    # ✅ Ensure only 6 columns are returned
    return ha_df[["timestamp", "open", "high", "low", "close", "volume"]].values.tolist()

def convert_to_heikin_ashi(df):
    """
    Convert standard candlestick data to Heikin Ashi candles.
    """
    ha_df = df.copy()

    # Heikin Ashi Close
    ha_df["ha_close"] = (df["open"] + df["high"] + df["low"] + df["close"]) / 4

    # Initialize first HA Open as the average of the first candlestick
    ha_df.loc[0, "ha_open"] = (df.loc[0, "open"] + df.loc[0, "close"]) / 2

    # Compute the rest of HA Opens
    for i in range(1, len(df)):
        ha_df.loc[i, "ha_open"] = (ha_df.loc[i - 1, "ha_open"] + ha_df.loc[i - 1, "ha_close"]) / 2

    # Heikin Ashi High and Low
    ha_df["ha_high"] = ha_df[["ha_open", "ha_close", "high"]].max(axis=1)
    ha_df["ha_low"] = ha_df[["ha_open", "ha_close", "low"]].min(axis=1)

    # ✅ Keep only Heikin Ashi columns and remove old ones
    ha_df = ha_df[["timestamp", "ha_open", "ha_high", "ha_low", "ha_close", "volume"]]

    # ✅ Rename Heikin Ashi columns to match standard OHLCV format
    ha_df = ha_df.rename(columns={"ha_open": "open", "ha_high": "high", "ha_low": "low", "ha_close": "close"})

    return ha_df

