import requests
import time

def fetch_binance_price(symbol='BTCUSDT'):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    for i in range(5):
        price_data = fetch_binance_price()
        if "price" in price_data:
            print(f"[{i+1}] BTC Price: {price_data['price']}")
        else:
            print(f"[{i+1}] Error fetching price: {price_data.get('error', 'Unknown error')}")
        time.sleep(5)
