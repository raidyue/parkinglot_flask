# encoding=utf-8
__author__ = 'raidyue'
from flask_admin.contrib.sqla import ModelView
from . import admin
from ..models import db, User, Parkinglot

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Parkinglot, db.session))
