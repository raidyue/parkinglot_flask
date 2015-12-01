from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import current_user
from flask.ext.cache import Cache

db = SQLAlchemy()
cache = Cache()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    over = db.Column(db.String(128))
    email = db.Column(db.String(128))
    orders = db.relationship('Order', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def has_unfinished_order(self, parkinglot):
        orders = db.session.query(User).filter_by(id=self.id).order_by('order_time')

    def __unicode__(self):
        return self.username

    @classmethod
    def is_exist(cls, username):
        return User.query.filter_by(username=username).first() != None

    @classmethod
    def get_user_by(cls, username):
        user = User.query.filter_by(username=username).first()
        return user if user else None


class Parkinglot(db.Model):
    __tablename__ = 'parkinglot'

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    city = db.Column(db.String(128))
    address = db.Column(db.String(128))
    charge = db.Column(db.String(128))

    orders = db.relationship('Order', backref='parkinglot')
    lots = db.relationship('Lot', backref='parkinglot')


class Lot(db.Model):
    __tablename__ = 'lot'

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    num = db.Column(db.INTEGER)
    status = db.Column(db.SMALLINT)

    p_id = db.Column(db.BIGINT, db.ForeignKey('parkinglot.id'))
    orders = db.relationship('Order', backref='lot')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DATETIME)
    end_time = db.Column(db.DATETIME)
    order_time = db.Column(db.DATETIME)
    status = db.Column(db.SMALLINT)

    p_id = db.Column(db.BIGINT, db.ForeignKey('parkinglot.id'))
    lot_id = db.Column(db.BIGINT, db.ForeignKey('lot.id'))
    user_id = db.Column(db.BIGINT, db.ForeignKey('user.id'))
