from trading.mexc_client import client
from config.config import TRADE_SYMBOL, TRADE_QUANTITY, PAPER_TRADING

# Paper trading account balance
virtual_balance = 1000.0
virtual_holdings = 0  # BTC held
virtual_short_position = 0  # Short position
entry_price = None  # Store the last trade entry price

def place_order(side, price):
    """
    Execute a market buy, sell, short, or cover order.

    :param side: "BUY", "SELL", "SHORT", or "COVER"
    :param price: Simulated price of execution
    """
    global virtual_balance, virtual_holdings, virtual_short_position, entry_price

    if PAPER_TRADING:
        if side == "BUY":
            if virtual_balance >= price * TRADE_QUANTITY:
                virtual_balance -= price * TRADE_QUANTITY
                virtual_holdings += TRADE_QUANTITY
                entry_price = price
                print(f"📊 Paper Trade: Bought {TRADE_QUANTITY} BTC at ${price:.2f}")
            else:
                print("⚠️ Not enough virtual balance to buy.")
        
        elif side == "SELL":
            if virtual_holdings >= TRADE_QUANTITY:
                virtual_balance += price * TRADE_QUANTITY
                virtual_holdings -= TRADE_QUANTITY
                print(f"📊 Paper Trade: Sold {TRADE_QUANTITY} BTC at ${price:.2f}")
            else:
                print("⚠️ Not enough BTC to sell.")
        
        elif side == "SHORT":
            virtual_short_position += TRADE_QUANTITY
            entry_price = price
            print(f"📊 Paper Trade: Opened SHORT position with {TRADE_QUANTITY} BTC at ${price:.2f}")
        
        elif side == "COVER":
            if virtual_short_position >= TRADE_QUANTITY:
                virtual_balance += (entry_price - price) * TRADE_QUANTITY  # Profit calculation
                virtual_short_position -= TRADE_QUANTITY
                print(f"📊 Paper Trade: Covered SHORT at ${price:.2f}")
            else:
                print("⚠️ No short position to cover.")
        
        print(f"💰 Virtual Balance: ${virtual_balance:.2f} | BTC Holdings: {virtual_holdings:.4f} BTC | Short Position: {virtual_short_position}")

    else:
        # Execute real order via API
        try:
            response = client.new_order(
                symbol=TRADE_SYMBOL, 
                side="SELL" if side == "SHORT" else side,  # SHORT will execute as SELL in API
                orderType="MARKET", 
                options={"quantity": TRADE_QUANTITY}
            )
            print(f"✅ Real Order Executed: {response}")
        except Exception as e:
            print(f"❌ Error placing real order: {e}")

