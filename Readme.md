# TradeBot

## Overview

TradeBot is an automated trading bot that executes trades using **Relative Strength Index (RSI), Bollinger Bands, Moving Averages (SMA), and MACD** to make informed Long and Short trades. The bot checks the market **every second** and follows strict risk management rules, including **Stop Loss (-1.5%) and Take Profit (+3%)**.

## Features

- **Supports Long & Short Trading** (Buy & Sell positions)
- **Technical Indicators**: RSI, Bollinger Bands, MACD, SMA (50 & 200)
- **Configurable Stop Loss & Take Profit**
- **Trade Cooldown Period** to prevent overtrading
- **Paper Trading Mode** (Dry-run with virtual balance)

## Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/TradeBot.git
cd TradeBot
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Set Up API Keys**

Create a `.env` file in the project directory and add:

```ini
MEXC_API_KEY=your_api_key
MEXC_API_SECRET=your_api_secret
```

## Configuration

Edit `config/config.py` to adjust trade settings:

```python
CHECK_INTERVAL = 1  # Check market every second
STOP_LOSS_PERCENT = 1.5  # Stop loss threshold (1.5%)
TAKE_PROFIT_PERCENT = 3.0  # Take profit threshold (3%)
COOLDOWN_PERIOD = 30  # Wait 30 seconds before placing another order
ENABLE_SHORT_TRADING = True  # Enable Short Selling
```

## Running the Bot

```bash
python3 main.py
```

## Trading Strategy

### **Long (BUY) Conditions**

✅ RSI < 30 (Oversold)✅ Price at or below Lower Bollinger Band✅ SMA 50 > SMA 200 (Uptrend)✅ MACD > MACD Signal (Bullish Confirmation)✅ Not in Cooldown Period

### **Long Exit (SELL) Conditions**

✅ RSI > 70 (Overbought)✅ Price at or above Upper Bollinger Band✅ Profit >= 3% or Stop Loss (-1.5%) hit✅ SMA 50 < SMA 200 (Trend Reversal)✅ MACD < MACD Signal (Bearish Confirmation)

### **Short (SELL) Conditions**

✅ RSI > 70 (Overbought)✅ Price at or above Upper Bollinger Band✅ SMA 50 < SMA 200 (Downtrend)✅ MACD < MACD Signal (Bearish Confirmation)✅ Not in Cooldown Period

### **Short Exit (COVER) Conditions**

✅ RSI < 30 (Oversold)✅ Price at or below Lower Bollinger Band✅ Profit >= 3% or Stop Loss (-1.5%) hit✅ SMA 50 > SMA 200 (Trend Reversal)✅ MACD > MACD Signal (Bullish Confirmation)

## Logs & Trade Tracking

All trades and errors are logged in `logs/bot.log`.

```bash
tail -f logs/bot.log
```

## Future Improvements

- **Real-time P&L tracking**
- **Backtesting support**
- **Customizable trade alerts**

---

🚀 Developed by Christopher Vega

