import pandas as pd
import numpy as np
from indicators.bollinger import calculate_bollinger_bands
from indicators.rsi import calculate_rsi
from indicators.stoch_rsi import calculate_stoch_rsi
from indicators.atr import calculate_atr
from indicators.moving_average import calculate_sma, calculate_ema, calculate_dema, calculate_tema

def trade_logic(data):
    """
    Trading strategy based on Heikin Ashi candles.
    """
    try:
        # ✅ Convert all values to float
        formatted_data = [[float(value) for value in row] for row in data]
        df = pd.DataFrame(formatted_data, columns=["timestamp", "open", "high", "low", "close", "volume"])

        # ✅ Extract price columns (Now using Heikin Ashi close)
        close_prices = df["close"].tolist()
        high_prices = df["high"].tolist()
        low_prices = df["low"].tolist()

        # Ensure we have enough data points
        if len(close_prices) < 3:
            return "HOLD"

        # Compute indicators using HA close prices
        bband_lower, bband_middle, bband_upper = calculate_bollinger_bands(df)
        rsi = calculate_rsi(df)
        atr = calculate_atr(df)
        stoch_k, stoch_d = calculate_stoch_rsi(df["close"])

        # Momentum logic (Now using HA close)
        momentum = stoch_k.iloc[-1] - stoch_k.iloc[-2]
        momentum_prev = stoch_k.iloc[-2] - stoch_k.iloc[-3]

        if stoch_k.iloc[-1] > 95 or stoch_k.iloc[-1] < 5:
            if momentum > 1:
                return "BUY"
            elif momentum < -1:
                return "SHORT"
        else:
            if momentum > 0:
                return "BUY"
            elif momentum < 0:
                return "SHORT"

        return "HOLD"

    except Exception as e:
        print(f"❌ Error in trade_logic(): {e}")
        return "ERROR"

