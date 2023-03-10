import requests
from twilio.rest import Client
import os

STOCK_NAME = "BLK"
COMPANY_NAME = "Blackrock"
NEWS_ARTICLES_RECEIVED = 3
MINIMUM_CHANGE = 5
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
USER_PHONE_NUMBER =os.getenv("MY_NUMBER")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

sentiment_parameters = {
    "function": "NEWS_SENTIMENT",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
# sentiment_response = requests.get(STOCK_ENDPOINT, params=sentiment_parameters)
# sentiment_data = sentiment_response.json()
# sentiment_data_list = [value for (key, value) in sentiment_data.items()]
# print(sentiment_data_list)


# Get yesterday's closing stock price.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
print(data)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the absolute (positive) difference between yesterdays' and the days before yesterdays' closing price.
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_or_down = None
if difference > 0:
    up_or_down = "⬆️"
elif difference < 0:
    up_or_down = "⬇️"
else:
    up_or_down = "↔️"


# Calculate the percentage change in price between the closing price yesterday and the day before yesterday.
percentage_diff = (difference / float(yesterday_closing_price)) * 100
print(percentage_diff)

# If percentage is greater than the users chosen amount then use the News API to get articles related to the COMPANY.
if abs(percentage_diff) > MINIMUM_CHANGE:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    # Use the slice operator to create a list containing the first 3 articles.
    three_articles = articles[:NEWS_ARTICLES_RECEIVED]
    print(three_articles)

    # Create a new list of the first 3 article's headlines and descriptions.
    formatted_articles = [f"\n{STOCK_NAME}: {up_or_down}{abs(round(percentage_diff, 2))}%\nHeadline: {article['title']}.\nURL: {article['url']}" for article in three_articles]

    # Send each article as a separate SMS.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE_NUMBER
        )
