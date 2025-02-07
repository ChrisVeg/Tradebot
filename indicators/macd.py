import pandas as pd
import ta

def calculate_macd(data):
    """
    Calculate the MACD indicator.
    
    :param data: List of price candles
    :return: Latest MACD and MACD signal line values
    """
    df = pd.DataFrame(
        data,
        columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "ignore"]
    )
    df["close"] = df["close"].astype(float)
    macd_indicator = ta.trend.MACD(df["close"])
    return macd_indicator.macd().iloc[-1], macd_indicator.macd_signal().iloc[-1]

