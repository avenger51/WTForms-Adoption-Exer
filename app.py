from flask import Flask, render_template, flash, redirect, render_template, url_for
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pets

from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "pet adoption 1234"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/")
def homepage():
    """Show homepage links."""
    

    pets = Pets.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add_pet_form", methods=["GET", "POST"])
def add_pet():
    """Handles Adding A Pet."""

    form = AddPetForm()

    if form.validate_on_submit():  
        name = form.name.data   
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
         
        #check if this is necessary with forms...
        new_pet = Pets(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available
        )

        db.session.add(new_pet)
        db.session.commit()
        
        

        flash(f"Added {name} at {species}")
        return redirect("/")
    
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/edit_pet/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):

    pet = Pets.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('homepage'))

    else:
       # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)

