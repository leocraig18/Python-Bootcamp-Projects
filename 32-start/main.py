import smtplib
import datetime as dt
import random

my_email = "leopythontests@gmail.com"
my_password = "ptvnperwjffsizei"


def send_quote():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="leopythontests@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}."
        )
        print(quote)


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as quotes:
        quotes_list = [quote for quote in quotes]
        quote = random.choice(quotes_list)
    print(quotes_list)
    send_quote()
