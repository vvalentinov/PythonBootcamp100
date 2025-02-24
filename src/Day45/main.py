import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

headings = list(reversed(soup.find_all("h3", class_="title")))

with open("movies.txt", "w", encoding="utf-8") as file:
    for heading in headings:
        file.write(f"{heading.getText()}\n")


