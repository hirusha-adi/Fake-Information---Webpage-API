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
    company = profile["company"]
    ssn = profile["ssn"]
    residence = profile["residence"]
    current_location = profile["current_location"]
    blood_group = profile["blood_group"]
    username = profile["username"]
    address = profile["address"]
    mail = profile["mail"]

    mothers_maiden_name = fake.first_name_female()
    phone_number = fake.phone_number()

    # Zodiac Sign
    all_zodiac_signs = ("Aries", "Taurus", "Gemini", "Cancer", "Leo",
                        "Virgo", "Libra", "Scorpius", "Sagittarius",
                        "Capricornus", "Aquarius", "Pisces"
                        )
    tropical_zodiac = random.choice(all_zodiac_signs)

    birthdate = profile["birthdate"]
    proper_birthdate = datetime.datetime.now() - datetime.timedelta(days=int(age)*365)
    proper_age = str(proper_birthdate.strftime('%Y')) + "-" + \
        '-'.join(str(birthdate).split('-')[1:])

    # Password
    if random.choice((True, False)):
        password = "".join(random.sample(ascii_letters +
                                         digits + punctuation, random.randint(8, 16)))
    else:
        password = "".join(random.sample(ascii_letters +
                                         digits, random.randint(8, 16)))

    # Credit Card (CC)
    credit_card = fake.credit_card_full()
    cc_provider = str(credit_card).split("\n")[0]
    cc_number = str(credit_card).split("\n")[2].split(" ")[0]
    cc_expiry = str(credit_card).split("\n")[2].split(" ")[1]
    cc_cvv = str(credit_card).split("\n")[3]

    # More others
    color = fake.color_name()
    user_agent = fake.user_agent()
    company_email = fake.company_email()

    height = random.randint(159, 178)
    height_inch = str(int(height)/2.54)[:4]
    height_feet = str(int(height)/30.48)[:4]
    weight = random.randint(55, 89)
    weight_lbs = str(int(weight)*2.205)[:5]

    fake.add_provider(VehicleProvider)
    vehicle = fake.vehicle_year_make_model_cat()

    # Location
    # http://alvarestech.com/temp/routeconverter/RouteConverter/navigation-formats/src/main/doc/googlemaps/Google_Map_Parameters.htm
    # https://stackoverflow.com/questions/5807063/url-to-a-google-maps-page-to-show-a-pin-given-a-latitude-longitude
    current_location1 = str(current_location[0])
    current_location2 = str(current_location[1])

    return render_template("index.html",
                           first_name=first_name,
                           last_name=last_name,
                           name_info_gender=name_info_gender,
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
                           cc_cvv=cc_cvv,
                           cc_expiry=cc_expiry,
                           color=color,
                           company_email=company_email,
                           height=height,
                           height_inch=height_inch,
                           height_feet=height_feet,
                           weight=weight,
                           vehicle=vehicle,
                           weight_lbs=weight_lbs
                           )


# /api
@app.route("/api", methods=["GET"])
def api():
    final_reurn_val = {}
    # The face
    face = requests.get("https://fakeface.rest/face/json").json()
    final_reurn_val["age"] = face["age"]
    final_reurn_val["face_url"] = face["image_url"]
    final_reurn_val["gender"] = face["gender"]

    if str(final_reurn_val["gender"]).lower() == "male":
        final_reurn_val["name_info_gender"] = "boy"
    else:
        final_reurn_val["name_info_gender"] = "girl"

    # The fake profile
    fake = Faker()
    profile = fake.profile()

    # The name based on the gender of the image
    if str(final_reurn_val["gender"]).lower() == "male":
        final_reurn_val["first_name"] = fake.first_name_male()
        final_reurn_val["last_name"] = fake.last_name_male()
    else:
        final_reurn_val["first_name"] = fake.first_name_female()
        final_reurn_val["last_name"] = fake.last_name_female()

    final_reurn_val["job"] = profile["job"]
    final_reurn_val["company"] = profile["company"]
    final_reurn_val["ssn"] = profile["ssn"]
    final_reurn_val["residence"] = profile["residence"]
    final_reurn_val["blood_group"] = profile["blood_group"]
    final_reurn_val["username"] = profile["username"]
    final_reurn_val["address"] = profile["address"]
    final_reurn_val["mail"] = profile["mail"]

    final_reurn_val["mothers_maiden_name"] = fake.first_name_female()
    final_reurn_val["phone_number"] = fake.phone_number()

    # Zodiac Sign
    all_zodiac_signs = ("Aries", "Taurus", "Gemini", "Cancer", "Leo",
                        "Virgo", "Libra", "Scorpius", "Sagittarius",
                        "Capricornus", "Aquarius", "Pisces"
                        )
    final_reurn_val["tropical_zodiac"] = random.choice(all_zodiac_signs)

    birthdate = profile["birthdate"]
    proper_birthdate = datetime.datetime.now(
    ) - datetime.timedelta(days=int(final_reurn_val["age"])*365)
    final_reurn_val["proper_age"] = str(proper_birthdate.strftime('%Y')) + "-" + \
        '-'.join(str(birthdate).split('-')[1:])

    # Password
    if random.choice((True, False)):
        final_reurn_val["password"] = "".join(random.sample(ascii_letters +
                                                            digits + punctuation, random.randint(8, 16)))
    else:
        final_reurn_val["password"] = "".join(random.sample(ascii_letters +
                                                            digits, random.randint(8, 16)))

    # Credit Card (CC)
    credit_card = fake.credit_card_full()
    final_reurn_val["cc_provider"] = str(credit_card).split("\n")[0]
    final_reurn_val["cc_number"] = str(credit_card).split("\n")[
        2].split(" ")[0]
    final_reurn_val["cc_expiry"] = str(credit_card).split("\n")[
        2].split(" ")[1]
    final_reurn_val["cc_cvv"] = str(credit_card).split("\n")[3]

    # More others
    final_reurn_val["color"] = fake.color_name()
    final_reurn_val["user_agent"] = fake.user_agent()
    final_reurn_val["company_email"] = fake.company_email()

    final_reurn_val["height"] = random.randint(159, 178)
    final_reurn_val["height_inch"] = str(
        int(final_reurn_val["height"])/2.54)[:4]
    final_reurn_val["height_feet"] = str(
        int(final_reurn_val["height"])/30.48)[:4]
    final_reurn_val["weight"] = random.randint(55, 89)
    final_reurn_val["weight_lbs"] = str(
        int(final_reurn_val["weight"])*2.205)[:5]

    fake.add_provider(VehicleProvider)
    final_reurn_val["vehicle"] = fake.vehicle_year_make_model_cat()

    # Others
    final_reurn_val[
        "name_meaning_link"] = f"https://www.babysfirstdomain.com/meaning/{final_reurn_val['name_info_gender']}/{final_reurn_val['first_name']}"
    final_reurn_val[
        "current_location_google_maps_link"] = f"http://maps.google.com/maps?q={final_reurn_val['current_location1']},{final_reurn_val['current_location2']}"

    # Location
    # http://alvarestech.com/temp/routeconverter/RouteConverter/navigation-formats/src/main/doc/googlemaps/Google_Map_Parameters.htm
    # https://stackoverflow.com/questions/5807063/url-to-a-google-maps-page-to-show-a-pin-given-a-latitude-longitude
    current_location = profile["current_location"]
    final_reurn_val["current_location1"] = str(current_location[0])
    final_reurn_val["current_location2"] = str(current_location[1])

    return final_reurn_val


# Errors ------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3331, debug=True)
