from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
i=0
scores=[]

title = soup.select(selector=".titleline")
values = [tag.text for tag in title]

link = soup.select(selector=".titleline a")
values1 = [tag.get("href") for tag in link]

points = soup.select(selector=".subline")
values2 = [tag.text for tag in points]

for titles,links,points in zip(values,values1,values2):
    score_match = re.search('\d+', points)
    score = int(score_match.group())
    scores.append(score)
max_score=max(scores)

for titles,links,points in zip(values,values1,values2):
    score_match = re.search('\d+', points)
    score = int(score_match.group())
    if(score)==max_score:
        print("-----------------------Max Points:-----------------------\n")
        print("Article Title: \n")
        print(titles)
        print("\n\nArticle Link: \n")
        print(links)
        print("\n\nArticle Points: ")
        print(points)
        print("\n---------------------------------------------------------")
        