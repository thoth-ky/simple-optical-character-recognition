import os
from os.path import join, dirname, realpath
import pathlib
from flask import Blueprint, render_template, request, current_app

from ocr_core.ocr import ocr_core
from helpers.helpers import allowed_file

UPLOAD_FOLDER = '/static/uploads/'

uploads_blueprint = Blueprint('uploads_page', __name__)

# route and function to handle the upload page
@uploads_blueprint.route('/upload', methods=['GET', 'POST'])
def upload_page():
  if request.method == 'POST':
    # check if there is a file in the request
    if 'file' not in request.files:
      return render_template('upload.html', msg='No file selected')
    file = request.files['file']

    # if no file is selected
    if file.filename == '':
      return render_template('upload.html', msg='No file selected')

    if file and allowed_file(file.filename):
      # save uploaded file

      filepath = os.path.join(
        dirname(current_app.instance_path),
        current_app.config["UPLOAD_FOLDER"],
        file.filename
      )

      pathlib.Path(
        dirname(filepath)
      ).mkdir(exist_ok=True)

      file.save(filepath)
      # call the OCR function on it
      extracted_text = ocr_core(file)

      # extract the text and display it
      return render_template(
        'upload.html',
        msg='Successfully processed',
        extracted_text=extracted_text,
        img_src=current_app.config["UPLOAD_FOLDER"] + file.filename
      )

  elif request.method == 'GET':
    return render_template('upload.html')
