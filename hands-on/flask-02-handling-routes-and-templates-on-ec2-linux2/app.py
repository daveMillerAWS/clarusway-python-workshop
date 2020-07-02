from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')

def home():
    return "This is home for no path, <h1> Welcome Home </h1>"

@app.route('/about')
def about():
    return "<h1> This is my about page </h1>"

@app.route('/error')
def error():
    return "<h1> Either you encounter an error or you are not authorized </h1>"

@app.route("/hello")
def hello():
    return "<h1> Hello world </h1>"

@app.route("/admin")
def admin():
    return redirect(url_for('error'))


if __name__ == '__main__':
   # app.run(debug=True)
    app.run('0.0.0.0', port=80)