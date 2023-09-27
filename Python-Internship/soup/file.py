from bs4 import BeautifulSoup

file=open("index.html")
cont=file.read()
file.close()
soup = BeautifulSoup(cont, "html.parser")
print(soup.h1)
print(soup.a)


