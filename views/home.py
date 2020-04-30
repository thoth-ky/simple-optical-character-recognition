from flask import Blueprint, render_template

home_blueprint = Blueprint('home_page', __name__)

@home_blueprint.route('/')
def home_page():
    return render_template('index.html')