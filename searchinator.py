from GoogleNews import GoogleNews
from datetime import datetime as dt
import datetime
import json

categories = ["policies", "education", "biology", "economy", "statistics", "donations"]
def v1(county, state):

    location = (county + ", " + state)

    urls = [[],[],[],[],[],[]]

    now = dt.now()
    today_date = now.strftime("%m/%d/%Y")
    week_ago_date = (now - datetime.timedelta(days = 7)).strftime("%m/%d/%Y")

    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews = GoogleNews(start=week_ago_date,end=today_date)

    
    queries = [
        str(location) + " COVID-19 " + categories[0] + " news",
        str(location) + " COVID-19 " + categories[1] + " news",
        "Global COVID-19 Vaccine",
        str(location) + " COVID-19 " + categories[3] + " news",
        str(location) + " COVID-19 " + categories[4] + " news",
        str(location) + " COVID-19 " + categories[5]
    ]

    for query in queries:
        index = queries.index(query)
        googlenews = GoogleNews()
        googlenews.setlang('en')
        googlenews = GoogleNews(start=week_ago_date,end=today_date)
        googlenews.search(query)
        results = googlenews.result()
        res = results
        for i in range(len(res)-1):
            urls[index].append(results[i]['link'])


    success_string = "True"



    data = {
        "county": county,
        "state": state,
        "success": success_string,
        # "time": {
        #     "timestamp": now,
        # },
        "data": {
            "policies": {
                "urls": urls[0],
            },
            "education": {
                "urls": urls[1],
            },
            "biology": {
                "urls": urls[2],
            },
            "economy": {
                "urls": urls[3],
            },
            "statistics": {
                "urls": urls[4],
            },
            "donations": {
                "urls": urls[5],
            },
        },
    }
    return data
