import urllib
import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def searcher(county, category):
    google_query = (county + " covid-19 " + category + " news").replace(' ', '+')
    url = "https://google.com/search?q=" + google_query
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(url, headers=headers)
    urls = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        for i in soup.find_all('div', class_='r'):
            anchor = i.find_all('a')
            if anchor:
                myurl = anchors[0]['href']
                urls.append(myurl)
        return urls[:5]
