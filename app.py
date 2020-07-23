from flask import *
app = Flask(__name__)
import json

@app.route('/')
def home():
    with open('corpus.json') as f:
        data = json.load(f)
        print (data['attributes'][0]['test'])
        tester = data['attributes'][0]['test']
    return render_template("index.html", tester=tester)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")

@app.route('/mobile')
def mobile():
    return render_template("mobile.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
