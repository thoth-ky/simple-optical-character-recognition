import os

from flask import Flask, render_template

from ocr_core.ocr import ocr_core
from helpers.helpers import allowed_file
from views.home import home_blueprint

app = Flask(__name__)

UPLOAD_FOLDER = '/static/uploads/'

with app.app_context():

    app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run()