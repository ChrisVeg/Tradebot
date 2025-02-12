import pandas as pd
import ta

def calculate_bollinger_bands(data, window=20, std_dev=2):
    """
    Calculate Bollinger Bands.
    
    :param data: List of price candles
    :param window: Moving average window size (default: 20)
    :param std_dev: Standard deviation multiplier (default: 2)
    :return: (lower_band, middle_band, upper_band)
    """
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})  # Convert all to float

    bb = ta.volatility.BollingerBands(df["close"], window=window, window_dev=std_dev)
    return bb.bollinger_lband().iloc[-1], bb.bollinger_mavg().iloc[-1], bb.bollinger_hband().iloc[-1]


