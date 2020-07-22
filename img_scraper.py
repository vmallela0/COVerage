from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def img_scraper(url):
  img_urls = []
  html = urlopen(url)
  bs = BeautifulSoup(html, 'html.parser')
  images = bs.find_all('img', {'src':re.compile('.jpg')})
  for image in images: 
    img_urls.append(image['src'])
  return img_urls[0]
