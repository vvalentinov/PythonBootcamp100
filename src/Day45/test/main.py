from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

anchor_links = soup.select(selector=".titleline > a:first-of-type")
scores = soup.select(selector=".score")

for i in range(len(anchor_links)):
    score = int(scores[i].getText().split(' ')[0])
    print(f"{anchor_links[i].get("href")}  {score}")
