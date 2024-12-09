from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.get('/')
def index():
    return render_template('home.html')