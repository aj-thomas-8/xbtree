from flask import Flask
import nltk
from nltk.corpus import brown
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def render():
    word = brown.tagged_words()[8]

    return f"""<p>X-bar parse tree generator</p>
    <p>Sample brown word {escape(word)}</p>"""
