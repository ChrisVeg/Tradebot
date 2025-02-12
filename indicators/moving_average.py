import pandas as pd
import ta

def calculate_sma(data, window=50):
    """
    Calculate Simple Moving Average (SMA).

    :param data: List of closing prices
    :param window: SMA window size (default: 50)
    :return: Latest SMA value
    """
    df = pd.DataFrame(data, columns=["close"])
    df["close"] = df["close"].astype(float)
    return ta.trend.SMAIndicator(df["close"], window=window).sma_indicator().iloc[-1]

def calculate_ema(data, window=9):
    """
    Calculate Exponential Moving Average (EMA).

    :param data: List of closing prices
    :param window: EMA window size (default: 9)
    :return: Latest EMA value
    """
    df = pd.DataFrame(data, columns=["close"])
    df["close"] = df["close"].astype(float)
    return ta.trend.EMAIndicator(df["close"], window=window).ema_indicator().iloc[-1]

def calculate_dema(data, window=9):
    """
    Calculate Double Exponential Moving Average (DEMA).

    :param data: List of closing prices
    :param window: DEMA window size (default: 9)
    :return: Latest DEMA value
    """
    df = pd.DataFrame(data, columns=["close"])
    df["close"] = df["close"].astype(float)
    e1 = ta.trend.EMAIndicator(df["close"], window=window).ema_indicator()
    e2 = ta.trend.EMAIndicator(e1, window=window).ema_indicator()
    return 2 * e1.iloc[-1] - e2.iloc[-1]

def calculate_tema(data, window=9):
    """
    Calculate Triple Exponential Moving Average (TEMA).

    :param data: List of closing prices
    :param window: TEMA window size (default: 9)
    :return: Latest TEMA value
    """
    df = pd.DataFrame(data, columns=["close"])
    df["close"] = df["close"].astype(float)
    e1 = ta.trend.EMAIndicator(df["close"], window=window).ema_indicator()
    e2 = ta.trend.EMAIndicator(e1, window=window).ema_indicator()
    e3 = ta.trend.EMAIndicator(e2, window=window).ema_indicator()
    return 3 * (e1.iloc[-1] - e2.iloc[-1]) + e3.iloc[-1]

