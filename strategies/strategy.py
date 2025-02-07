import time
from indicators.rsi import calculate_rsi
from indicators.bollinger import calculate_bollinger_bands
from indicators.moving_average import calculate_sma
from indicators.macd import calculate_macd
from config.config import STOP_LOSS_PERCENT, TAKE_PROFIT_PERCENT, COOLDOWN_PERIOD, ENABLE_SHORT_TRADING

# Track last trade execution time and last trade action
last_trade_time = 0
last_trade_action = None
entry_price = None  # Store entry price for risk management

def trade_logic(data):
    """
    Define a safe and accurate trading strategy with Long and Short positions.

    :param data: List of price candles
    :return: "BUY", "SELL", "SHORT", "COVER" or "HOLD"
    """
    global last_trade_time, last_trade_action, entry_price

    # Get latest market data
    rsi = calculate_rsi(data)
    lower_band, middle_band, upper_band = calculate_bollinger_bands(data)
    sma_50 = calculate_sma(data, 50)  # 50-period SMA
    sma_200 = calculate_sma(data, 200)  # 200-period SMA
    macd, macd_signal = calculate_macd(data)
    last_close = float(data[-1][5])  # Latest closing price
    current_time = time.time()

    # Check if we are in a cooldown period
    if current_time - last_trade_time < COOLDOWN_PERIOD:
        return "HOLD"

    # **LONG (BUY) CONDITIONS**
    if (
        rsi < 30 and last_close <= lower_band and  # Oversold & Bollinger band confirmation
        sma_50 > sma_200 and  # Uptrend confirmation
        macd > macd_signal  # MACD bullish signal
        and last_trade_action != "BUY"  # Avoid consecutive buys
    ):
        last_trade_time = current_time
        last_trade_action = "BUY"
        entry_price = last_close  # Store entry price
        return "BUY"

    # **LONG EXIT (SELL) CONDITIONS**
    if (
        last_trade_action == "BUY" and
        (rsi > 70 or last_close >= upper_band or last_close >= entry_price * (1 + TAKE_PROFIT_PERCENT / 100))
    ):
        last_trade_time = current_time
        last_trade_action = "SELL"
        return "SELL"

    # **SHORT (SELL FIRST) CONDITIONS**
    if ENABLE_SHORT_TRADING and (
        rsi > 70 and last_close >= upper_band and  # Overbought & Bollinger band confirmation
        sma_50 < sma_200 and  # Downtrend confirmation
        macd < macd_signal  # MACD bearish signal
        and last_trade_action != "SHORT"  # Avoid consecutive shorts
    ):
        last_trade_time = current_time
        last_trade_action = "SHORT"
        entry_price = last_close
        return "SHORT"

    # **SHORT EXIT (COVER) CONDITIONS**
    if (
        last_trade_action == "SHORT" and
        (rsi < 30 or last_close <= lower_band or last_close <= entry_price * (1 - TAKE_PROFIT_PERCENT / 100))
    ):
        last_trade_time = current_time
        last_trade_action = "COVER"
        return "COVER"

    return "HOLD"

