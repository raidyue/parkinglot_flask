from flask import Flask

from app.models import db
from app.core.views import main_bp
from app.manager.views import manager_bp
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    register_database(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(manager_bp)
    return app


def register_database(app):
    db.init_app(app)
    db.app = app
