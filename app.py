from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
