from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("a")
print(tags[1])