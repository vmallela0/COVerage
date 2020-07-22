from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
