import os
import platform

import requests
from faker import Faker
from flask import Flask, request, render_template, redirect

if os.name == 'posix':
    CLEAR = "clear"
    SLASH = "/"
else:
    CLEAR = "clear"
    SLASH = "\\"

app = Flask(__name__)


# / ------------------------------
@app.route("/", methods=["GET"])
def index():
    face = requests.get("https://fakeface.rest/face/json").json()
    age = face["age"]
    face_url = face["image_url"]


# Errors ------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3331, debug=True)
