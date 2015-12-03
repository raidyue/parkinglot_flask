# encoding=utf-8
__author__ = 'raidyue'
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import BaseView, expose
from flask_admin import Admin
from ..models import db, User, Parkinglot

admin = Admin(name='parkinglot', template_mode='bootstrap3')


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


admin.add_view(MyView(name='MyView'))
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Parkinglot, db.session))
