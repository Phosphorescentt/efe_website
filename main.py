import hashlib

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import forms

from config import SECRETS


app = Flask(__name__, template_folder="public")
app.config["SECRET_KEY"] = SECRETS.SECRET_KEY
Bootstrap(app)


cred = credentials.Certificate("config/firebase_admin_sdk_key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://esports-fixtures-emailer-default-rtdb.europe-west1.firebasedatabase.app/",
    "databaseAuthVariableOverride": {
        "uid": "website"
        }
    })

emails_ref = db.reference("emails")

@app.route("/", methods=["GET", "POST"])
def index():
    form = forms.EmailGamesForm()

    if form.validate_on_submit():
        email = form.email.data
        valorant = form.valorant.data
        league_of_legends = form.league_of_legends.data

        # build the dict object
        h = hashlib.md5(bytes(email, "utf-8")).hexdigest()
        o = {
                h: {
                    "email": email,
                    "games": {
                        "valorant": valorant,
                        "league_of_legends": league_of_legends
                        }
                    }
                }


        # set the json object in the database
        emails_ref.set(o)

        return render_template("index.html", subscribed=True)

    return render_template("index.html", subscribed=False, form=form)

