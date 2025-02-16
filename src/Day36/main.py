import requests
import datetime as dt
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_api_response = requests.get(url=STOCK_API_ENDPOINT, params=stock_api_params)
stock_api_response.raise_for_status()
stock_data = stock_api_response.json()

last_refreshed_as_text = stock_data["Meta Data"]["3. Last Refreshed"]
last_refreshed_as_date = dt.datetime.strptime(last_refreshed_as_text, "%Y-%m-%d").date()
day_before_last_refreshed_as_text = (last_refreshed_as_date - dt.timedelta(days=1)).strftime("%Y-%m-%d")

closing_price_last_refreshed = float(stock_data["Time Series (Daily)"][last_refreshed_as_text]["4. close"])
closing_price_day_before_last_refreshed = float(stock_data["Time Series (Daily)"][day_before_last_refreshed_as_text]["4. close"])

diff = closing_price_last_refreshed - closing_price_day_before_last_refreshed
abs_diff = abs(diff)
diff_percentage = round((abs_diff / closing_price_last_refreshed) * 100)

up_down_emoji = "🔺" if diff > 0 else "🔻"

if diff_percentage > 5:
    news_api_params = {
        "q": "tesla",
        "qInTitle": COMPANY_NAME,
        "from": last_refreshed_as_text,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }

    news_api_response = requests.get(url=NEWS_API_ENDPOINT, params=news_api_params)
    news_api_response.raise_for_status()
    news_data = news_api_response.json()
    articles = news_data["articles"][:3]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(
            body=f"{STOCK}: {up_down_emoji} {diff_percentage}%\n{article["title"]}\nBrief: {article["description"]}",
            from_="some number here",
            to="some number here",
        )
