import requests
import time

def fetch_price(symbol_id='bitcoin'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol_id}&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {"price": data[symbol_id]['usd']}
    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    for i in range(5):
        price_data = fetch_price()
        if "price" in price_data:
            print(f"[{i+1}] Bitcoin Price: ${price_data['price']}")
        else:
            print(f"[{i+1}] Error fetching price: {price_data.get('error', 'Unknown error')}")
        time.sleep(5)
