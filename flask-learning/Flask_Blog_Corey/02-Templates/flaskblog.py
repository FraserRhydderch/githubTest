from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Question 1',
        'title': 'This is the first question',
        'content': 'More info here',
        'date_posted': 'June 30, 2022'
    },
    {
        'author': 'Question 2',
        'title': 'This is the second question',
        'content': 'More info here',
        'date_posted': 'April 21, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
