from trading.mexc_client import client
from config.config import START_BALANCE

# Simulated trading state
virtual_balance = START_BALANCE  # Start with configured balance
btc_holdings = 0.0  # BTC owned
short_position = 0.0  # Short position in BTC
last_trade = None  # Track last executed trade (BUY or SHORT)


def place_order(order_type, price):
    global virtual_balance, btc_holdings, short_position, last_trade

    total_value = (btc_holdings + short_position) * price + virtual_balance  # Net worth

    if order_type == "BUY":
        if virtual_balance > 0 and last_trade != "BUY":  # Prevent multiple buys
            btc_holdings = virtual_balance / price  # Buy max BTC with available balance
            virtual_balance = 0.0  # Update balance to zero
            last_trade = "BUY"  # Track last trade
            print(f"🚀 BUY Order | Price: ${price:.4f} | Holdings: {btc_holdings:.4f} BTC")
    
    elif order_type == "SELL":
        if btc_holdings > 0:
            virtual_balance = btc_holdings * price  # Convert BTC back to USD
            btc_holdings = 0.0  # Reset BTC holdings
            last_trade = "SELL"
            print(f"🔻 SELL Order | Price: ${price:.4f} | Balance: ${virtual_balance:.2f}")
    
    elif order_type == "SHORT":
        if btc_holdings > 0:
            place_order("SELL", price)  # Sell BTC before shorting

        if virtual_balance > 0 and last_trade != "SHORT":  # Prevent multiple shorts
            short_position = virtual_balance / price  # Open a short position
            virtual_balance = 0.0  # Zero out balance after shorting
            last_trade = "SHORT"
            print(f"📉 SHORT Opened | Price: ${price:.4f} | Short Position: {short_position:.4f} BTC")
    
    elif order_type == "COVER":
        if short_position > 0:
            virtual_balance = short_position * price  # Convert short position back to USD
            short_position = 0.0  # Reset short position
            last_trade = "COVER"
            print(f"📈 SHORT Closed | Price: ${price:.4f} | Balance: ${virtual_balance:.2f}")

    # Print **only** trade summary (not raw data)
    print(f"💰 Balance: ${virtual_balance:.2f} | BTC Holdings: {btc_holdings:.4f} BTC | Short: {short_position:.4f} BTC")
    print(f"📊 Net Worth: ${total_value:.2f}")



