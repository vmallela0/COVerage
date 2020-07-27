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
        location = request.form['location']
        print(location)

    return render_template(
        "index.html",
        lavaa = lavaa
    )


@app.route('/about')
def about():
    return render_template("about.html")

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
