from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

#tags = soup.select(selector=".hname a")
tags = soup.select(selector=".pagetop a")
values = [tag.text for tag in tags]
for text in values:
    print(text)
