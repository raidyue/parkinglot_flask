__author__ = 'raidyue'

from flask.ext.script import Manager

from app import create_app
from app.models import db

app = create_app()

manager = Manager(app)


@manager.command
def create_db():
    db.drop_all()
    db.create_all()

@manager.command
def reflect_db():
    db.reflect()



if __name__ == '__main__':
    manager.run()
