from flask import Flask
from main.config import config_by_name
def create_app(config_name):
    app = Flask(__name__,template_folder='templates')
    app.config.from_object(config_by_name[config_name])
    #db.init_app(app)
    return app