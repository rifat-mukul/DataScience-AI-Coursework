from pycoingecko import CoinGeckoAPI

# Debugging: Indicate script start
print("Script started...")

# Initialize the CoinGeckoAPI client
cg = CoinGeckoAPI()

# Fetch the current price of Bitcoin in USD
bitcoin_price = cg.get_price(ids='bitcoin', vs_currencies='usd')

# Debugging: Print the fetched data
print("Fetched data:", bitcoin_price)

# Check if the data is correctly fetched
if bitcoin_price and 'bitcoin' in bitcoin_price and 'usd' in bitcoin_price['bitcoin']:
    print(f"The current price of Bitcoin in USD is: ${bitcoin_price['bitcoin']['usd']}")
else:
    print("Failed to fetch Bitcoin price.")
