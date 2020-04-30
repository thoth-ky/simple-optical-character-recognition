from os.path import join
from flask import Blueprint, render_template, send_from_directory, current_app

home_blueprint = Blueprint('home_page', __name__)

@home_blueprint.route('/')
def home_page():
    return render_template('index.html')


@home_blueprint.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(
      join(current_app.root_path, 'static'),
      'favicon.ico',
      mimetype='image/vnd.microsoft.icon'
    )