import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

TARGET_PRICE = 100
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}

response = requests.get(
    url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",
    headers=headers
)

soup = BeautifulSoup(response.content, "html.parser")

price_as_str = soup.select_one(selector=".a-offscreen").get_text()
price = float(price_as_str.split("$")[1])

product_title = soup.select_one(selector="h1#title #productTitle").getText().strip()

if price <= TARGET_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now {price}! Hurry and buy it!".encode('utf-8'))