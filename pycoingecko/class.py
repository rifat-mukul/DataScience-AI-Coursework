from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id = "bitcoin", vs_currency= "usd", days=2)
print(bitcoin_data['prices'])