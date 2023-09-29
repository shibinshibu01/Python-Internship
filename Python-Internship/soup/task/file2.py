from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")


title = soup.select(selector=".titleline")
values = [tag.text for tag in title]

link = soup.select(selector=".titleline a")
values1 = [tag.get("href") for tag in link]

points = soup.select(selector=".subline")
values2 = [tag.text for tag in points]

for titles,links,points in zip(values,values1,values2):
    print("------Article Title------")
    print(titles)
    print("\n------Article Link------")
    print(links)
    print("\n------Article Points------")
    print(points)
    print("\n\n")