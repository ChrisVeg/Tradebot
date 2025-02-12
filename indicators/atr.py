import pandas as pd

def calculate_atr(data, period=14):
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})  # Convert all to float

    df['tr'] = df[['high', 'low', 'close']].max(axis=1) - df[['high', 'low', 'close']].min(axis=1)
    df['atr'] = df['tr'].rolling(window=period).mean()
    return df['atr'].iloc[-1]


