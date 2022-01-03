import datetime
import os
import platform
import random
from string import ascii_letters, punctuation, digits

import requests
from faker import Faker
from flask import Flask, redirect, render_template, request
from faker_vehicle import VehicleProvider

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
    RAND = random.choice((True, False))

    # The face
    face = requests.get("https://fakeface.rest/face/json").json()
    age = face["age"]
    face_url = face["image_url"]
    gender = face["gender"]

    if str(gender).lower() == "male":
        name_info_gender = "boy"
    else:
        name_info_gender = "girl"

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

    # Additional
    mothers_maiden_name = fake.first_name_female()
    phone_number = fake.phone_number()

    all_zodiac_signs = ("Aries", "Taurus", "Gemini", "Cancer", "Leo",
                        "Virgo", "Libra", "Scorpius", "Sagittarius",
                        "Capricornus", "Aquarius", "Pisces"
                        )
    tropical_zodiac = random.choice(all_zodiac_signs)

    proper_birthdate = datetime.datetime.now() - datetime.timedelta(days=int(age)*365)
    proper_age = str(proper_birthdate.strftime('%Y')) + "-" + \
        '-'.join(str(birthdate).split('-')[1:])

    if RAND:
        password = "".join(random.sample(ascii_letters +
                                         digits + punctuation, random.randint(8, 16)))
    else:
        password = "".join(random.sample(ascii_letters +
                                         digits, random.randint(8, 16)))

    user_agent = fake.user_agent()

    # Credit Card (CC)
    credit_card = fake.credit_card_full()
    cc_provider = str(credit_card).split("\n")[0]
    cc_number = str(credit_card).split("\n")[2].split(" ")[0]
    cc_expiry = str(credit_card).split("\n")[2].split(" ")[1]
    cc_cvc = str(credit_card).split("\n")[3]

    # More others
    color = fake.color_name()
    company_email = fake.company_email()

    height = random.randint(159, 178)
    weight = random.randint(55, 89)

    fake.add_provider(VehicleProvider)
    vehicle = fake.vehicle_year_make_model_cat()

    # Location
    # http://alvarestech.com/temp/routeconverter/RouteConverter/navigation-formats/src/main/doc/googlemaps/Google_Map_Parameters.htm
    # https://stackoverflow.com/questions/5807063/url-to-a-google-maps-page-to-show-a-pin-given-a-latitude-longitude
    current_location1 = str(current_location[0])
    current_location2 = str(current_location[1]).split("'")

    return render_template("index.html",
                           first_name=first_name,
                           last_name=last_name,
                           job=job,
                           birthdate=proper_age,
                           company=company,
                           ssn=ssn,
                           residence=residence,
                           current_location1=current_location1,
                           current_location2=current_location2,
                           blood_group=blood_group,
                           username=username,
                           address=address,
                           mail=mail,
                           age=age,
                           face_url=face_url,
                           mothers_maiden_name=mothers_maiden_name,
                           phone_number=phone_number,
                           tropical_zodiac=tropical_zodiac,
                           password=password,
                           user_agent=user_agent,
                           cc_provider=cc_provider,
                           cc_number=cc_number,
                           cc_cvc=cc_cvc,
                           cc_expiry=cc_expiry,
                           color=color,
                           company_email=company_email,
                           height=height,
                           weight=weight,
                           vehicle=vehicle,
                           name_info_gender=name_info_gender
                           )


# Errors ------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3331, debug=True)
