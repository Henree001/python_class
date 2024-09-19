import requests
from bs4 import BeautifulSoup


url = "https://appclick.ng/portal/site/login"

response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
title = soup.title.text
# print(title)
div = soup.div.contents
print(div)
print(soup.link['href'])
print(soup.link['rel'])
print(soup.link['type'])
print(soup.div.name)