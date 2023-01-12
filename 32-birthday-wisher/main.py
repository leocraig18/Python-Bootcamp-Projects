import random
import pandas
import datetime as dt
import smtplib
import os

PLACEHOLDER = "[NAME]"
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")


def send_quote(email, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{message}."
        )


now = dt.date.today()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        final_message = contents.replace(PLACEHOLDER, (birthday_person["name"]))
        send_quote(birthday_person["email"], final_message)




