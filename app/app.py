from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('home.html')