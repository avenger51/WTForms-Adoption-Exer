"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import NumberRange, InputRequired, EqualTo, Optional, Email, Length, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name") 
    #basic : species = SelectField("Pet Species") #not working: [validators.EqualTo("cat", message="Species must be 'cat'")])
    #not working: species = StringField("Pet Species", [InputRequired("cat", message="Species must be 'cat'")])
    species = SelectField(
        "Species",
        choices=[("Hedgehog", "Hedgehog"), ("Dog", "Dog"), ("Bunny", "Bunny")],
    )
    photo_url = StringField("Pet Photo URL", validators=[URL()],
    ) 
    #basic: age = FloatField("Pet Age")
    age = IntegerField(
        "Age",
        validators=[NumberRange(min=0, max=30)],
    )
    notes = StringField("Pet Notes")
    available = BooleanField("Is Available")
  
class EditPetForm(FlaskForm):
    """Form for adding pets"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
