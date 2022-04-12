from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class EmailGamesForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    valorant = BooleanField("VALORANT")
    league_of_legends = BooleanField("League Of Legends")
    submit = SubmitField("Subscribe")
