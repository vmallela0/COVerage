# data for index => feeds data from searcher.py and model
import json
import requests
from searchinator import *
from flask import Flask
from flask import request
from flask import render_template
from searchinator import *
import nltk
from newspaper import Article
from newspaper import fulltext
app = Flask(__name__)

headline_policies_1 = headline_policies_2 = headline_policies_3 = headline_policies_4 = headline_policies_5 = " default"

headline_education_1 = headline_education_2 = headline_education_3 = headline_education_4 = headline_education_5 = " default"

headline_biology_1 = headline_biology_2 = headline_biology_3 = headline_biology_4 = headline_biology_5 = " default"

headline_economy_1 = headline_economy_2 = headline_economy_3 = headline_economy_4 = headline_economy_5 = " default"

headline_statistics_1 = headline_statistics_2 = headline_statistics_3 = headline_statistics_4 = headline_statistics_5 = " default"
# Paragraphs
text_policies_1 = text_policies_2 = text_policies_3 = text_policies_4 = text_policies_5 = "text about policies"

text_education_1 = text_education_2 = text_education_3 = text_education_4 = text_education_5 = "text about education"

text_biology_1 = text_biology_2 = text_biology_3 = text_biology_4 = text_biology_5 = "text about biology"

text_economy_1 = text_economy_2 = text_economy_3 = text_economy_4 = text_economy_5 = "text about economy"

text_statistics_1 = text_statistics_2 = text_statistics_3 = text_statistics_4 = text_statistics_5 = "text about statistics"

text_donations_1 = text_donations_2 = text_donations_3 = text_donations_4 = text_donations_5 = "Donate to help fight COVID-19"

# images
img_policies_1 = img_policies_2 = img_policies_3 = img_policies_4 = img_policies_5 = "https://imgur.com/lNhUEmK.png"

img_education_1 = img_education_2 = img_education_3 = img_education_4 = img_education_5 = "https://imgur.com/KiDWiTr.png"

img_biology_1 = img_biology_2 = img_biology_3 = img_biology_4 = img_biology_5 = "https://imgur.com/aY2TasC.png"

img_economy_1 = img_economy_2 = img_economy_3 = img_economy_4 = img_economy_5 = "https://imgur.com/W9kLJHc.png"

img_statistics_1 = img_statistics_2 = img_statistics_3 = img_statistics_4 = img_statistics_5 = "https://imgur.com/8IzNJTT.png"

# urls
url_policies_1 = url_policies_2 = url_policies_3 = url_policies_4 = url_policies_5 = "https://compression.stanford.edu/"

url_education_1 = url_education_2 = url_education_3 = url_education_4 = url_education_5 = "https://compression.stanford.edu/"

url_biology_1 = url_biology_2 = url_biology_3 = url_biology_4 = url_biology_5 = "https://compression.stanford.edu/"

url_economy_1 = url_economy_2 = url_economy_3 = url_economy_4 = url_economy_5 = "https://compression.stanford.edu/"

url_statistics_1 = url_statistics_2 = url_statistics_3 = url_statistics_4 = url_statistics_5 = "https://compression.stanford.edu/"

url_donations_1 = url_donations_2 = url_donations_3 = url_donations_4 = url_donations_5 = "https://covid19responsefund.org/en/"
# tag names
tag1_policies_1 = tag1_policies_2 = tag1_policies_3 = tag1_policies_4 = tag1_policies_5 = "policies tag1"

tag1_education_1 = tag1_education_2 = tag1_education_3 = tag1_education_4 = tag1_education_5 = "edu tag1"

tag1_biology_1 = tag1_biology_2 = tag1_biology_3 = tag1_biology_4 = tag1_biology_5 = "bio tag1"

tag1_economy_1 = tag1_economy_2 = tag1_economy_3 = tag1_economy_4 = tag1_economy_5 = "econ tag1"

tag1_statistics_1 = tag1_statistics_2 = tag1_statistics_3 = tag1_statistics_4 = tag1_statistics_5 = "stat tag1"

tag2_policies_1 = tag2_policies_2 = tag2_policies_3 = tag2_policies_4 = tag2_policies_5 = "policies tag2"

tag2_education_1 = tag2_education_2 = tag2_education_3 = tag2_education_4 = tag2_education_5 = "edu tag2"

tag2_biology_1 = tag2_biology_2 = tag2_biology_3 = tag2_biology_4 = tag2_biology_5 = "bio tag2"

tag2_economy_1 = tag2_economy_2 = tag2_economy_3 = tag2_economy_4 = tag2_economy_5 = "econ tag2"

tag2_statistics_1 = tag2_statistics_2 = tag2_statistics_3 = tag2_statistics_4 = tag2_statistics_5 = "stat tag2"

tag3_policies_1 = tag3_policies_2 = tag3_policies_3 = tag3_policies_4 = tag3_policies_5 = "policies tag3"

tag3_education_1 = tag3_education_2 = tag3_education_3 = tag3_education_4 = tag3_education_5 = "edu tag3"

tag3_biology_1 = tag3_biology_2 = tag3_biology_3 = tag3_biology_4 = tag3_biology_5 = "bio tag3"

tag3_economy_1 = tag3_economy_2 = tag3_economy_3 = tag3_economy_4 = tag3_economy_5 = "econ tag3"

tag3_statistics_1 = tag3_statistics_2 = tag3_statistics_3 = tag3_statistics_4 = tag3_statistics_5 = "stat tag3"




lavaa = {
    "policies":
        {
            "url": [
                url_policies_1,
                url_policies_2,
                url_policies_3,
                url_policies_4,
                url_policies_5
            ],
            "image": [
                img_policies_1,
                img_policies_2,
                img_policies_3,
                img_policies_4,
                img_policies_5
            ],
            "text": [
                text_policies_1,
                text_policies_2,
                text_policies_3,
                text_policies_4,
                text_policies_5
            ],
            "headlines": [
                headline_policies_1,
                headline_policies_2,
                headline_policies_3,
                headline_policies_4,
                headline_policies_5
            ],
            "tags": [
                [tag1_policies_1,
                tag2_policies_1,
                tag3_policies_1],

                [tag1_policies_2,
                tag2_policies_2,
                tag3_policies_2],

                [tag1_policies_3,
                tag2_policies_3,
                tag3_policies_3],

                [tag1_policies_4,
                tag2_policies_4,
                tag3_policies_4],

                [tag1_policies_5,
                tag2_policies_5,
                tag3_policies_5]
            ]

        },
    "education":
        {
            "url": [
                url_education_1,
                url_education_2,
                url_education_3,
                url_education_4,
                url_education_5
            ],
            "image": [
                img_education_1,
                img_education_2,
                img_education_3,
                img_education_4,
                img_education_5
            ],
            "text": [
                text_education_1,
                text_education_2,
                text_education_3,
                text_education_4,
                text_education_5
            ],
            "headlines": [
                headline_education_1,
                headline_education_2,
                headline_education_3,
                headline_education_4,
                headline_education_5
            ],
            "tags": [
                [tag1_education_1,
                tag2_education_1,
                tag3_education_1],

                [tag1_education_2,
                tag2_education_2,
                tag3_education_2],

                [tag1_education_3,
                tag2_education_3,
                tag3_education_3],

                [tag1_education_4,
                tag2_education_4,
                tag3_education_4],

                [tag1_education_5,
                tag2_education_5,
                tag3_education_5]
            ]

        },
    "biology":
        {
            "url": [
                url_biology_1,
                url_biology_2,
                url_biology_3,
                url_biology_4,
                url_biology_5
            ],
            "image": [
                img_biology_1,
                img_biology_2,
                img_biology_3,
                img_biology_4,
                img_biology_5
            ],
            "text": [
                text_biology_1,
                text_biology_2,
                text_biology_3,
                text_biology_3,
                text_biology_4,
                text_biology_5
            ],
            "headlines": [
                headline_biology_1,
                headline_biology_2,
                headline_biology_3,
                headline_biology_4,
                headline_biology_5
            ],
            "tags": [
                [tag1_biology_1,
                tag2_biology_1,
                tag3_biology_1],

                [tag1_biology_2,
                tag2_biology_2,
                tag3_biology_2],

                [tag1_biology_3,
                tag2_biology_3,
                tag3_biology_3],

                [tag1_biology_4,
                tag2_biology_4,
                tag3_biology_4],

                [tag1_biology_5,
                tag2_biology_5,
                tag3_biology_5]
            ]

        },
    "economy":
        {
            "url": [
                url_economy_1,
                url_economy_2,
                url_economy_3,
                url_economy_4,
                url_economy_5
            ],
            "image": [
                img_economy_1,
                img_economy_2,
                img_economy_3,
                img_economy_4,
                img_economy_5
            ],
            "text": [
                text_economy_1,
                text_economy_2,
                text_economy_3,
                text_economy_4,
                text_economy_5
            ],
            "headlines": [
                headline_economy_1,
                headline_economy_2,
                headline_economy_3,
                headline_economy_4,
                headline_economy_5
            ],
            "tags": [
                [tag1_economy_1,
                tag2_economy_1,
                tag3_economy_1],

                [tag1_economy_2,
                tag2_economy_2,
                tag3_economy_2],

                [tag1_economy_3,
                tag2_economy_3,
                tag3_economy_3],

                [tag1_economy_4,
                tag2_economy_4,
                tag3_economy_4],

                [tag1_economy_5,
                tag2_economy_5,
                tag3_economy_5]
            ]

        },
    "statistics":
        {
            "url": [
                url_statistics_1,
                url_statistics_2,
                url_statistics_3,
                url_statistics_4,
                url_statistics_5
            ],
            "image": [
                img_statistics_1,
                img_statistics_2,
                img_statistics_3,
                img_statistics_4,
                img_statistics_5
            ],
            "text": [
                text_statistics_1,
                text_statistics_2,
                text_statistics_3,
                text_statistics_4,
                text_statistics_5
            ],
            "headlines": [
                headline_statistics_1,
                headline_statistics_2,
                headline_statistics_3,
                headline_statistics_4,
                headline_statistics_5
            ],
            "tags": [
                [tag1_statistics_1,
                tag2_statistics_1,
                tag3_statistics_1],

                [tag1_statistics_2,
                tag2_statistics_2,
                tag3_statistics_2],

                [tag1_statistics_3,
                tag2_statistics_3,
                tag3_statistics_3],

                [tag1_statistics_4,
                tag2_statistics_4,
                tag3_statistics_4],

                [tag1_statistics_5,
                tag2_statistics_5,
                tag3_statistics_5]
            ]
        }, 
        "donations":
        {
            "url": [
                url_donations_1,
                url_donations_2,
                url_donations_3,
                url_donations_4,
                url_donations_5
            ],
            "text": [
                text_donations_1, 
                text_donations_2, 
                text_donations_3, 
                text_donations_4, 
                text_donations_5
            ]
        }
}


@app.route('/', methods=['GET','POST'])
def home():
    if(request.method == 'POST'):
        jsdata = request.form
        print(jsdata)
        send_urls("Santa Clara", "California")
        # rescor = coord(jsdata['county_name'] , jsdata['state_code'])
        
    return render_template(
        "index.html",
        lavaa = lavaa, 
    )

def coord(geolat, geolong):
    geolat = str(geolat)
    geolong = str(geolong)
    x = requests.get("https://geo.fcc.gov/api/census/area?lat=" + geolat + "&lon=" + geolong)
    data = (x.json())
    if(len(data['results']) != 0): return [data['results'][0]['county_name'],  data['results'][0]['state_name']]
    else: return ["global", "international"]

def img_scrape(url_list):
    arrayinator = []
    for url in url_list:
        arrayinator.append(img_scraper(url))
    return arrayinator

def popinator(lst, index):
    lst.append(lst.pop(index)) # moves element to end of list

cat_list = ['policies', 'education', 'biology','economy', 'statistics']
# search => urls
def send_urls(county_name, state_code):
    # try:
    url_data = v1(county_name, state_code)
    for i in cat_list:
        lavaa[i]['url'] = url_data['data'][i]['urls']
        for r in range(5):
            article = Article(str(lavaa[i]['url'][r]))
            
            try:
                article.download()
                article.parse()
                article.nlp()
                lavaa[i]['headlines'][r] = article.title
                lavaa[i]['image'][r] = article.top_image
                lavaa[i]['text'][r] = article.summary
                lavaa[i]['tags'][r] = article.keywords[0:2]
            except:
                lavaa[i]['headlines'][r] = "Error"
                lavaa[i]['text'][r] = "default text"
                lavaa[i]['tags'][r] = ['1' ,'2', '3']
                continue

    print("success")
    


# send_urls("SantaClara", "CA") #! use this for testing
# print(lavaa)
# res = requests.get("https://coveragee-api.herokuapp.com/api/v1/Fulton/GA")
# url_data = res.json()
# print(url_data)