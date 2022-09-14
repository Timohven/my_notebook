#from import_DB import find_note, get_all_notes
from flask import Flask, redirect, request, render_template, flash
from flask_cors import CORS
import datetime, json
from get_json_from_MySQL import get_all, update_note, add_note

app = Flask(__name__, static_url_path='')
CORS(app)

app.config.update(
    DEBUG=True,
    TESTING=True,
    TEMPLATES_AUTO_RELOAD=True
    )

#csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'any secret string'

@app.before_request
def before_request():
    app.jinja_env.cache = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/notes')
def notes():
    get_all()
    return render_template("notes.json")

@app.route('/calendar')
def calendar():
    dt = str(datetime.datetime.now())
    d = dict(now=dt)
    print(d)
    json.dump(d, open("templates/dict.json", "w"))
    return render_template("dict.json")

@app.route('/update', methods=['POST'])
def update():
    res = request.get_json()
    print(res)
    update_note(res.get('data'))
    return (res)

@app.route('/add', methods=['POST'])
def add():
    res = request.get_json()
    print(res)
    add_note(res.get('data'))
    return (res)

if __name__ == "__main__":
    app.run()
