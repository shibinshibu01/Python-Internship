from bs4 import BeautifulSoup

file=open("index.html")
cont=file.read()
file.close()
soup = BeautifulSoup(cont, "html.parser")


tags = soup.find_all("a")
values = [tag.get("href") for tag in tags]
print(values)
