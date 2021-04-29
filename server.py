from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, AMANSARS!'


@app.route('/about.html')
def blog():
    return render_template('about.html')


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my Dog Blog Page'


@app.route('/blog/2020/fuck')
def blog3():
    return 'This is FUCK'


@app.route('/urltest/<username>/<int:post_id>')
def urlTest(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
