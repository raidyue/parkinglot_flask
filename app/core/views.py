# encoding=utf-8
from flask import Blueprint, render_template, request, session, url_for, redirect, flash, g
from models import User, db

main_bp = Blueprint('main', __name__)


@main_bp.route('/hello')
def hello():
    return render_template('helloworld.html')


@main_bp.route('/')
def index():
    username = session.get('username', None)
    return render_template('index.html', username=username)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    print 'method=%s' % request.method
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print username, password
        user = db.session.query(User).filter_by(username=username).first()
        if user:
            session['username'] = user.username
            flash(u'用户存在')
            return redirect(url_for('.index'))
        else:
            flash(u'该用户不存在')
            return render_template('login.html')
    else:
        return url_for('.index')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not User.is_exist(username):
            u = User(username=username, password=password)
            db.session.add(u)
            db.session.commit()
            session['username'] = username
            return redirect(url_for('.index'))
        else:
            flash(u'该用户已存在')
            return render_template('register.html')
    else:
        return url_for('.index')


@main_bp.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('.index'))


@main_bp.route('/add/<name>/<passwd>')
def create_user(name, passwd):
    u = User(username=name, password=passwd)
    db.session.add(u)
    db.session.commit()
    return 'success'
