import pandas
import datetime as dt
import smtplib
import random

now = dt.datetime.now()

df = pandas.read_csv("birthdays.csv")
data_dictionary = df.to_dict(orient="records")

for data in data_dictionary:
    if data["month"] == now.month and data["day"] == now.day:
        name = data["name"]
        to_email = data["email"]

        random_letter_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_letter_number}.txt", "r") as letter:
            letter_content = letter.read().strip()
            email_content = letter_content.replace("[NAME]", name)

        sender_email = "test@gmail.com"
        app_password = "app_password_here"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=app_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday!\n\n{email_content}")
