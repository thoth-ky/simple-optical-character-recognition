import os

from flask import Flask, render_template

from ocr_core.ocr import ocr_core

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()