from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "about page"

@app.route('/services')
def services():
    return "services page"

@app.route('/contact')
def contact():
    return "contact page"


if __name__ == '__main__':
    app.run(debug=True)
