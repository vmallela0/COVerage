from flask import *
app = Flask(__name__)
import json

@app.route('/')
def home():
    with open('corpus.json') as f:
        data = json.load(f)
        print (data['attributes'][0]['test'])
        tester = data['attributes'][0]['test']

    headline_policies_1 = "Policies 1"
    headline_policies_2 = "Policies 2"
    headline_policies_3 = "Policies 3"
    headline_policies_4 = "Policies 4"
    headline_policies_5 = "Policies 5"

    headline_education_1 = "Education 1"
    headline_education_2 = "Education 2"
    headline_education_3 = "Education 3"
    headline_education_4 = "Education 4"
    headline_education_5 = "Education 5"

    headline_biology_1 = "Biology 1"
    headline_biology_2 = "Biology 2"
    headline_biology_3 = "Biology 3"
    headline_biology_4 = "Biology 4"
    headline_biology_5 = "Biology 5"

    headline_economy_1 = "Economy 1"
    headline_economy_2 = "Economy 2"
    headline_economy_3 = "Economy 3"
    headline_economy_4 = "Economy 4"
    headline_economy_5 = "Economy 5"

    headline_statistics_1 = "Statistics 1"
    headline_statistics_2 = "Statistics 2"
    headline_statistics_3 = "Statistics 3"
    headline_statistics_4 = "Statistics 4"
    headline_statistics_5 = "Statistics 5"

    return render_template(
        "index.html",
        tester=tester,
        headline_policies_1 = headline_policies_1,
        headline_policies_2 = headline_policies_2,
        headline_policies_3 = headline_policies_3,
        headline_policies_4 = headline_policies_4,
        headline_policies_5 = headline_policies_5,

        headline_education_1 = headline_education_1,
        headline_education_2 = headline_education_2,
        headline_education_3 = headline_education_3,
        headline_education_4 = headline_education_4,
        headline_education_5 = headline_education_5,

        headline_biology_1 = headline_biology_1,
        headline_biology_2 = headline_biology_2,
        headline_biology_3 = headline_biology_3,
        headline_biology_4 = headline_biology_4,
        headline_biology_5 = headline_biology_5,

        headline_economy_1 = headline_economy_1,
        headline_economy_2 = headline_economy_2,
        headline_economy_3 = headline_economy_3,
        headline_economy_4 = headline_economy_4,
        headline_economy_5 = headline_economy_5,

        headline_statistics_1 = headline_statistics_1,
        headline_statistics_2 = headline_statistics_2,
        headline_statistics_3 = headline_statistics_3,
        headline_statistics_4 = headline_statistics_4,
        headline_statistics_5 = headline_statistics_5,

    )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")

@app.route('/mobile')
def mobile():
    return render_template("mobile.html")

@app.route('/location')
def location():
    return render_template("location.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
