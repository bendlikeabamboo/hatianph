from flask import Blueprint, render_template

contact = Blueprint('contact', __name__)

@contact.route("/email")
def email():
    return render_template("contact.jinja", text="Testing")
