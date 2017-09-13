from flask import Flask

flask_app = Flask(__name__, instance_relative_config=True)

from app import views

flask_app.config.from_object('config.MainConfig')
