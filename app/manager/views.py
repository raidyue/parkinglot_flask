# encoding=utf-8
__author__ = 'raidyue'
from flask import Blueprint, render_template, session, request
from ..models import *

manager_bp = Blueprint('manager', __name__, url_prefix='/manager', template_folder='templates')


@manager_bp.route('/')
def index():
    if 'manager' in session:
        return 'login manager'

    return render_template('htllo.html')


@manager_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('manager_login.html')
