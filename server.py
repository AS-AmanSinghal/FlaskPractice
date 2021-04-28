from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, RS!'


@app.route('/blog')
def blog():
    return 'This is my Blog Page'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my Dog Blog Page'
