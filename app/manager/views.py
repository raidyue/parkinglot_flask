# encoding=utf-8
__author__ = 'raidyue'
from flask import Blueprint,render_template,session
from ..models import *

manager_bp = Blueprint('manager', __name__, url_prefix='/manager', template_folder='templates')


@manager_bp.route('/')
def index():
    if 'manager' in session:
        pass

    return render_template('htllo.html')
