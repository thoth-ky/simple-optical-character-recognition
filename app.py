from flask import Flask, render_template

from views.home import home_blueprint
from views.uploads import uploads_blueprint

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = 'static/uploads/'

# extract to env depending on whether on dev
# maybe separate config file???

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["EXPLAIN_TEMPLATE_LOADING"] = True
app.config["DEBUG"] = True

with app.app_context():

    app.register_blueprint(home_blueprint)
    app.register_blueprint(uploads_blueprint)

if __name__ == '__main__':
    app.run()