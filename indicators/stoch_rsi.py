import pandas as pd

def calculate_stoch_rsi(close_prices, length=14, smooth_k=3, smooth_d=3):
    """
    Calculate Stochastic RSI.

    :param close_prices: Pandas Series of closing prices
    :param length: RSI period (default: 14)
    :param smooth_k: Stochastic %K smoothing period (default: 3)
    :param smooth_d: Stochastic %D smoothing period (default: 3)
    :return: Tuple of (stoch_k, stoch_d)
    """
    try:
        if len(close_prices) < length:
            print(f"❌ Error: Not enough data points for Stochastic RSI. Required: {length}, Available: {len(close_prices)}")
            return pd.Series(dtype="float64"), pd.Series(dtype="float64")  # Return empty series instead of -1


        # Calculate RSI
        rsi = close_prices.rolling(length).apply(lambda x: ((x[-1] - x.min()) / (x.max() - x.min())) * 100, raw=True)
        
        if rsi.isnull().all():
            print("❌ Error: NaN values detected in RSI calculation")
            return pd.Series(dtype="float64"), pd.Series(dtype="float64")  # Return empty series

        # Compute Stochastic RSI
        stoch_k = rsi.rolling(smooth_k).mean()
        stoch_d = stoch_k.rolling(smooth_d).mean()

        if stoch_k.dropna().empty or stoch_d.dropna().empty:
            print("❌ Error: Stochastic RSI calculation resulted in NaN values")
            return pd.Series(dtype="float64"), pd.Series(dtype="float64")  # Return empty series


        return stoch_k, stoch_d

    except Exception as e:
        print(f"❌ Error in calculate_stoch_rsi(): {e}")
        return pd.Series(dtype="float64"), pd.Series(dtype="float64")  # Return empty series


