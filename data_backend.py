from locate import *

# data for index

# declaring default values
headline_policies_1 = headline_policies_2 = headline_policies_3 = headline_policies_4 = headline_policies_5 = "Policies default"

headline_education_1 = headline_education_2 = headline_education_3 = headline_education_4 = headline_education_5 = "Education default"

headline_biology_1 = headline_biology_2 = headline_biology_3 = headline_biology_4 = headline_biology_5 = "Bio default"

headline_economy_1 = headline_economy_2 = headline_economy_3 = headline_economy_4 = headline_economy_5 = "Economy default"

headline_statistics_1 = headline_statistics_2 = headline_statistics_3 = headline_statistics_4 = headline_statistics_5 = "Stat default"

# Paragraphs
text_policies_1 = text_policies_2 = text_policies_3 = text_policies_4 = text_policies_5 = "text about policies"

text_education_1 = text_education_2 = text_education_3 = text_education_4 = text_education_5 = "text about education"

text_biology_1 = text_biology_2 = text_biology_3 = text_biology_4 = text_biology_5 = "text about biology"

text_economy_1 = text_economy_2 = text_economy_3 = text_economy_4 = text_economy_5 = "text about economy"

text_statistics_1 = text_statistics_2 = text_statistics_3 = text_statistics_4 = text_statistics_5 = "text about statistics"

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

county_name = get_county(get_location_data) 
# print(county_name)
county_fips = get_fips(get_location_data)
# print(county_fips)

lavaa = {
    "location":
        {
            "location": [
                county_name, # county name
                county_fips # county
            ]
        },
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

        }
}
