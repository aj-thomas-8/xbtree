import datetime
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import tagger
import subprocess
import os
import re

app = Flask(__name__)

page = 0

def remove_trees():
    for f in os.listdir('./static'):
        if re.search('.svg', f):
            os.remove('./static/' + f)

@app.route("/show_tree", methods=['GET', 'POST'])
def show_tree():
    image_names = []
    for f in os.listdir('./static'):
        if re.search('.svg', f):
            image_names += [f]

    return render_template('view.html', utc_dt=datetime.datetime.utcnow(), data=image_names)

@app.route("/index")
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['input_sentence']
        tagger.tag(sentence)

        remove_trees()

        subprocess.run(["./parse_xtree", "new_sentence.csv"])

        return redirect(url_for('show_tree'))

    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

