from flask import *
app = Flask(__name__)
import json
from data_backend import *

@app.route('/', methods=['GET','POST'])
def home():
    # with open('corpus.json') as f:
    #     data = json.load(f)
    #     print (data['attributes'][0]['test'])
    #     tester = data['attributes'][0]['test']
    if request.method == 'POST':
        jsdata = request.form
        print(jsdata['county_name'])
        print(jsdata['state_code'])


    return render_template(
        "index.html",
        lavaa = lavaa
    )


@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/donate')
def donate():
    return render_template("donate.html")

@app.route('/mobile')
def mobile():
    return render_template(
        "mobile.html",
        lavaa = lavaa
        )

@app.route('/location')
def location():
    return render_template("location.html")

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
