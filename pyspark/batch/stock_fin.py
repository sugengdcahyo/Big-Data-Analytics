import finnhub
import os
from dotenv import load_dotenv

load_dotenv()

# Setup client
print(os.getenv("FINNHUB_API_KEY"))
finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))

# Stock candles
# res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
news = finnhub_client.general_news('general')
print(len(news))