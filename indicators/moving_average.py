import pandas as pd
import ta

def calculate_sma(data, window=50):
    """
    Calculate Simple Moving Average (SMA).
    
    :param data: List of price candles
    :param window: SMA window size (default: 50)
    :return: Latest SMA value
    """
    df = pd.DataFrame(
        data,
        columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "ignore"]
    )
    df["close"] = df["close"].astype(float)
    return ta.trend.SMAIndicator(df["close"], window=window).sma_indicator().iloc[-1]


