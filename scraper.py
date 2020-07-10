import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
from collections import Counter
from textblob import stopwords
URL = 'https://www.mercurynews.com/2020/07/07/h-1b-san-jose-firm-will-pay-to-resolve-claim-it-favored-indian-applicants-over-white-applicants/'





whitelist = ['\t', '\n']
whitelist_summarization = ["the","of","&", "and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","its","now","find","long","down","day","did","get","come","made","may","part"]

summary = "Coronavirus (COVID-19) Main Web Page  This guidance was created through the statewide reopening schools  task force that fostered a collaborative process for our educators and stakeholders  to lend their important voices. Also informed by the technical assistance and  advice of many health and safety organizations including the Centers for  Disease Control, California Department of Public Health, California Division of  Occupational Safety and Health, the intent of this document is to be a guide  for the local discussion on safely reopening schools. Stronger Together Guidebook Video Overview  \u00a0 Stronger Together:\r  A Guidebook for the Safe Reopening of California's Public Schools(PDF; 4MB; Added 08-Jun-2020) CDE Locations CDE Mission CDE Organization Contact Us Equal Opportunity Jobs at CDE Newsroom Superintendent's Initiatives Meeting Agendas Meeting Minutes & Schedule Members California School Dashboard Common Core State Standards Complaint Procedures Content Standards Curriculum Resources Education Funding English Language Development Standards Financial Allocations & Apportionments High School Equivalency Tests High School Graduation Requirements Kindergarten in California Released Test Questions Social and Emotional Learning Standards & Frameworks Accountability - School Performance Career Technical Education Charter Schools Child Nutrition Child Development Disaster and Emergency Management  Expanded Learning Principal Apportionments Safe Schools School Facilities Special Education Standardized Testing Title I Title III California School Directory Education Calendars Education FAQs Language Access Complaint Laws & Regulations Multilingual Documents Publications School and District Reports >> More Resources A-Z Index | Site Map Web Policy Accessibility Certification \r\u00a9 California Department of Education"
split_sentences = summary.split()
Counter = Counter(split_sentences)
keywords = Counter.most_common(20)
keyList = []
for word in keywords:
    keyList.append(word[0]) if word[0] not in stopwords.words('english')]
    for delWord in whitelist_summarization:
        if(word == delWord):
            keyList.remove(word)
print(keyList)

training_urls = {
    "politics": [
        'https://www.sccgov.org/sites/covid19/Pages/home.aspx',
        'https://www.cupertino.org/our-city/city-news/coronavirus-covid-19',
        'https://www.santaclaraca.gov/i-want-to/stay-informed/current-topics/coronavirus-updates',
        'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/california-santa-clara-county.html',
        'https://www.sfchronicle.com/news/article/Coronavirus-FAQ-Should-you-wear-a-face-mask-15147298.php',
        'https://www.mercurynews.com/2020/05/20/santa-clara-county-now-requires-that-you-wear-a-face-covering-san-jose-wants-to-go-further/',
    ],
    "education": [
        'https://www.cde.ca.gov/ls/he/hn/strongertogether.asp',
        'https://www.sccoe.org/covid-19/Pages/latest-updates.aspx',
        'https://www.sfchronicle.com/bayarea/article/Bay-Area-high-school-students-miss-academic-15152197.php',
        'https://www.mercurynews.com/2020/05/28/california-school-districts-could-forego-attendance-standardized-tests-during-coronavirus-pandemic/',
        'https://abc7news.com/education/watch-today-state-superintendent-discusses-guidelines-to-reopen-schools-/6201690/'
    ],
    "biology": [
        'https://www.cidrap.umn.edu/news-perspective/2020/05/scientists-exactly-zero-evidence-covid-19-came-lab',
        'https://www.nature.com/articles/d41586-020-01449-8',
        'https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html#:~:text=The%20virus%20is%20thought%20to,are%20not%20showing%20symptoms.',
        'https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/animals.html',
        'https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker',
        'https://www.nytimes.com/interactive/2020/science/coronavirus-vaccine-tracker.html',
        'https://landing.google.com/screener/covid19',
        'https://www.sccgov.org/sites/covid19/Pages/covid19-testing.aspx',
        'https://www.cvs.com/minuteclinic/covid-19-testing'
    ],
    "economy": [
        'https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html',
        'https://www.mercurynews.com/2020/06/12/coronavirus-retail-valley-fair-oakridge-malls-prep-re-openings-economy-commercial-real-estate-jobs/',
        'https://sanjosespotlight.com/category/coronavirus/',
        'https://www.sccgov.org/sites/covid19/Pages/business-guidance.aspx',
        'https://www.sfchronicle.com/business/article/Out-of-work-because-of-coronavirus-These-15135747.php',
        'https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/unemployment/'
    ],
    "statistics": [
        'https://www.reporternewspapers.net/2020/06/26/june-26-atlanta-sandy-springs-covid-19-report-180-more-diagnoses-14-day-trend-is-up/',
        'https://www.fox5atlanta.com/news/georgia-coronavirus-cases-are-up-and-its-not-just-because-of-testing-doctors-say',
        'https://www.11alive.com/article/news/health/coronavirus/coronavirus-numbers/covid-19-in-georgia-numbers-june-24-cases/85-aed1f537-d064-47dd-84fc-bf1b7ac1e483',
        'https://www.11alive.com/article/news/health/coronavirus/coronavirus-numbers/covid-19-cases-in-atlanta-zip-code/85-d589e7e8-d6ef-4c43-988e-f418a5a1c01a',
        'https://www.wsbtv.com/news/local/atlanta/atlanta-mayor-says-city-is-experiencing-an-all-time-high-cases/MLZQDVZPCVC6LL6JYBZUMJK4BQ/',
        'https://wgxa.tv/news/coronavirus/hospitalizations-rise-as-georgia-virus-cases-hit-new-peak',
        'https://dph.georgia.gov/covid-19-daily-status-report'
    ],
}

def isNone(URL, category):
    r = requests.get(URL)
    type(r)
    html = r.text
    page = urlopen("https://www.vmallela.com/404") # change to ./404 for exceptions

    try:
        page = urlopen(URL)
    except:
        return True
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div')
    if(content == None):
        return True
    else:
        return False
def scrapeTransfer(URL, categrory):
    r = requests.get(URL)
    type(r)
    html = r.text
    page = urlopen("https://www.vmallela.com/404") # change to ./404 for exceptions

    try:
        page = urlopen(URL)
    except:
        return None
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div')
    if(soup.find('h1') == None):
        header = "error"
    else:
        header = soup.find('h1').get_text().strip()

    article = ''
    if(content == None):
            article = 'error'
    else:
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
        corpus = data[categrory]
        corpus.append(new_data)
    write_json(data)

for key, value in training_urls.items() :
    for url in value:
        if isNone(url, key) == False:
            scrapeTransfer(url, key)

# print(soup.p)
