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
    # The face
    face = requests.get("https://fakeface.rest/face/json").json()
    age = face["age"]
    face_url = face["image_url"]
    gender = face["gender"]

    # The fake profile
    fake = Faker()
    profile = fake.profile()

    # The name based on the gender of the image
    if str(gender).lower() == "male":
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()

    job = profile["job"]
    birthdate = profile["birthdate"]
    company = profile["company"]
    ssn = profile["ssn"]
    residence = profile["residence"]
    current_location = profile["current_location"]
    blood_group = profile["blood_group"]
    username = profile["username"]
    address = profile["address"]
    mail = profile["mail"]

    return render_template("index.html",
                           first_name=first_name,
                           last_name=last_name,
                           job=job,
                           birthdate=birthdate,
                           company=company,
                           ssn=ssn,
                           residence=residence,
                           current_location=current_location,
                           blood_group=blood_group,
                           username=username,
                           address=address,
                           mail=mail,
                           age=age,
                           face_url=face_url
                           )


# Errors ------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3331, debug=True)
