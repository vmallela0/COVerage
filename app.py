from flask import *
import nltk
nltk.download('punkt')

app = Flask(__name__)
import json
from data_backend import *

@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/donate')
def donate():
    return render_template("donate.html")

@app.route('/location')
def location():
    return render_template("location.html")

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
