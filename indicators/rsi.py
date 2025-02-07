import pandas as pd
import ta

def calculate_rsi(data, period=14):
    """
    Calculate the Relative Strength Index (RSI).
    
    :param data: List of price candles
    :param period: RSI period (default: 14)
    :return: Latest RSI value
    """
    df = pd.DataFrame(
        data,
        columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "ignore"]
    )
    df["close"] = df["close"].astype(float)  # Ensure numeric format
    return ta.momentum.RSIIndicator(df["close"], window=period).rsi().iloc[-1]

