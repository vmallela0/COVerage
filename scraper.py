import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = 'https://www.fox5atlanta.com/news/atlanta-mayor-to-sign-order-mandating-masks-to-fight-covid-19'

r = requests.get(URL)
type(r)
html = r.text

# Create a BeautifulSoup object from the HTML
try:
   page = urlopen(URL)
except:
   print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('div', {"class": "article-body"})

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text

print(article)

# print(soup.p)
