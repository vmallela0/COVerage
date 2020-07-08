import requests
from bs4 import BeautifulSoup

URL = 'https://www.fox5atlanta.com/news/atlanta-mayor-to-sign-order-mandating-masks-to-fight-covid-19'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
headline = soup.find("h1")
content = soup.find("article")
print(headline.prettify())
print(content.prettify())