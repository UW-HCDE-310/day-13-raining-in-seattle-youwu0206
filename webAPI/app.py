from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def check_is_it_raining():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_raining = response.read().decode()

    if is_raining == "true":
        return "<h1>Yes</h1>"
    else:
        return "<h1>No</h1>"



