import datetime as dt
import smtplib
import random

with open("../quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

random_quote = random.choice(quotes).strip()

my_email = "test@gmail.com"
app_password = "app_password_here"

now = dt.datetime.now()

if now.weekday() == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{random_quote}")


