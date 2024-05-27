
import pandas as pd
from pycoingecko import CoinGeckoAPI

# Initialize the CoinGeckoAPI client
cg = CoinGeckoAPI()

# Fetch historical market data for Bitcoin
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=2)

# Extract the 'prices' data
prices = bitcoin_data['prices']

# Convert the 'prices' data to a DataFrame
data = pd.DataFrame(prices, columns=["TimeStamp", "Price"])

# Convert the 'TimeStamp' to datetime and add it as a new column "Date"
data["Date"] = pd.to_datetime(data['TimeStamp'], unit='ms')

# Print the DataFrame to verify
print(data)
