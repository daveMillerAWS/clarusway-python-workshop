from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    print("Hello World")

if __name__ == "__main__":
    #app.run('localhost',port=5000, debug=True)
    app.run(debug=True)
    #app.run('0.0.0.0',port=80)
