import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = 'https://www.mercurynews.com/2020/07/07/h-1b-san-jose-firm-will-pay-to-resolve-claim-it-favored-indian-applicants-over-white-applicants/'

r = requests.get(URL)
type(r)
html = r.text

# Create a BeautifulSoup object from the HTML


try:
    page = urlopen(URL)
except:
    print("page not working")

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('div') # , {"class": "article-body"}
header = soup.find('h1')

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text

print(header)
print(article)

# print(soup.p)
