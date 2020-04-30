# INTRO

This project is inspired by [this](https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/) blog post.
It is an effort to build a simple Python OCR application served by a flask web app. It makes use of [pytesseract] (https://pypi.org/project/pytesseract/) which is a wrapper
for [Google's Tesseract-OCR ENgine](https://github.com/tesseract-ocr/tesseract). Future work on this will continue to make the application more robust providing more options as well as
improving on the OCR Engine.

## DEvelopment Environment

Development is done in:
1. WSL Ubuntu 18.04
2. Python 3.8.2
3. Tesseract 4.0.0-beta.1

## SETUP

1. Follow the instructions given [here](https://github.com/tesseract-ocr/tesseract/wiki#installation) to install the tesseract engine first
2. Clone this repository 
  ```bash
   $ https://github.com/thoth-ky/simple-optical-character-recognition.git
  ```

  ```bash
   $ cd simple-optical-character-recognition
  ```

3. Create a python virtual environment (Optional)
  ```bash
   $ virtualenv ocr-env
  ```
  ```bash
   $ source ocr-env/bin/activate
  ```
4. Install python dependencies
  ```bash
   $ pip install -r requirements.txt
  ```
5. Run the application. By default it will run on localhost port 5000
  ```bash
   $ python app.py
  ```
6. Go to http://localhost:5000/ in the homepage you'll find instructions on how to use the application

## DOCKER SETUP

-TODO

## Authors
 - Joseph Mutuku Kyalo

## Resources

I advance gratitude to developer/engineers and all teams involved in any capacity in the following projects
- Flask
- https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/
- https://tesseract-ocr.github.io/tessdoc/
- 

