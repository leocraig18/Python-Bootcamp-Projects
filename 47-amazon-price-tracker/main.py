import requests
from bs4 import BeautifulSoup
import smtplib
import os

url = "https://www.amazon.co.uk/PlayStation-5-Digital-Edition-Console/dp/B08H97NYGP/ref=sr_1_2?crid=1ZXFDL3NA94JL&keywords=playstation+5&qid=1673531064&sprefix=playstation+5%2Caps%2C91&sr=8-2"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(name="span", class_="a-size-large product-title-word-break").get_text()
print(title)

BUY_PRICE = 550

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.getenv("MY_EMAIL"), os.getenv("MY_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("MY_EMAIL"),
            to_addrs=os.getenv("MY_EMAIL"),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode('utf-8')
        )