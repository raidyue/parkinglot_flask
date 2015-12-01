from flask import Flask
from flask.ext.login import LoginManager
from app.core.models import db
from app.core.views import main_bp
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    app.register_blueprint(main_bp)
    register_database(app)
    return app


def register_database(app):
    db.init_app(app)
    db.app = app
