import pandas as pd
from mexc_sdk import Spot
from config.config import API_KEY, API_SECRET

client = Spot(api_key=API_KEY, api_secret=API_SECRET)

def get_klines(symbol, interval="1m", limit=100):
    """
    Fetch Kline (candlestick) data from MEXC API and return as list.
    
    :param symbol: Trading pair (e.g., "BTCUSDT")
    :param interval: Kline interval (e.g., "1m", "5m", "1h")
    :param limit: Number of data points to fetch
    :return: List of kline data formatted correctly
    """
    raw_data = client.klines(symbol=symbol, interval=interval, options={"limit": limit})

    # MEXC returns 8 columns, so we must correctly define all columns
    df = pd.DataFrame(
        raw_data,
        columns=[
            "timestamp", "open", "high", "low", "close", "volume", "close_time", "ignore"
        ]
    )

    # Convert necessary columns to float
    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df.values.tolist()  # Return list format for strategy processing

