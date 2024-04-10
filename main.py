import datetime
from flask import Flask, render_template
from markupsafe import escape
import nltk
from nltk.corpus import brown

app = Flask(__name__)

@app.route("/")
def render():
    return render_template('view.html', utc_dt=datetime.datetime.utcnow())
