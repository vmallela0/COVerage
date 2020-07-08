import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
URL = 'https://www.mercurynews.com/2020/07/07/h-1b-san-jose-firm-will-pay-to-resolve-claim-it-favored-indian-applicants-over-white-applicants/'

r = requests.get(URL)
type(r)
html = r.text


whitelist = ['\t', '\n']
# Create a BeautifulSoup object from the HTML


try:
    page = urlopen(URL)
except:
    print("page not working")

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('div') # , {"class": "article-body"}
header = soup.find('h1').get_text().strip()
#print(content)

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text

for b in whitelist:
    article = article.replace(b, '')

print(header)

def write_json(data, filename='corpus.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
        
new_data = {str(header) : str(article)}
with open('corpus.json') as json_file:
    data = json.load(json_file)
    corpus = data['corpus']
    corpus.append(new_data)
write_json(data)

# print(soup.p)
