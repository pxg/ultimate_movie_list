import json
import decimal
from models.database import db_session
from flask import Flask, Response, redirect, render_template, request, \
session, url_for
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.auth import Auth, AuthUser, login_required, logout
from models.sa import get_user_class
from combine_lists import *

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Auth and DB settings #########################################################
db = SQLAlchemy(app)


## Set SQL Alchemy to automatically tear down (remove session)
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

## Instantiate authentication
auth = Auth(app, login_url_name='login')
User = get_user_class(db.Model)


# Admin settings (should we move to it's own file)? ############################
class MyView(BaseView):
    def is_accessible(self):
        # can we force a redirect? just hides menu
        user = User.load_current_user()
        return user
        #return False

    @expose('/')
    def index(self):
        return self.render('admin/index.html')

admin = Admin(app, name='Ultimate Movie List Admin')
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))
admin.add_view(MyView(name='IMDB Movies'))


# JSON generation (should we move to it's own file)? ###########################
class DecimalEncoder(json.JSONEncoder):
    """
    Required to stop annoying problem with json.dumps and decimal types
    http://stackoverflow.com/questions/8652497/caught-typeerror-while-rendering-decimal51-8-is-not-json-serializable
    """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


def json_api_response(list):
    """
    json output for api
    """
    return Response(json.dumps(list, cls=DecimalEncoder),
                    mimetype='application/json')


# Auth views ###################################################################
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter(User.username == username).first()
        if user is not None:
            # Authenticate and log in!
            if user.authenticate(request.form['password']):
                session['username'] = request.form['username']
                #TODO: we should force the admin url here
                return redirect(url_for('index'))
            else:
                flash('Incorrect password. Please try again')
                return render_template('login.html')
        else:
            flash('Incorrect username. Please try again')
            return render_template('login.html')
    return render_template('login.html')


def logout_view():
    user_data = logout()
    if user_data is None:
        msg = 'No user to log out.'
        return render_template('logout.html', msg=msg)
    else:
        msg = 'Logged out user {0}.'.format(user_data['username'])
        return render_template('logout.html', msg=msg)


# Actual Ultimate Film List Views (should we move to it's own file)? ###########
@login_required()
def index():
    return render_template('index.html')


@app.route('/ultimate-list')
def ultimate_list():
    film_list = get_ultimate_movie_list()
    if request.args.get('format') == 'json':
        return json_api_response(film_list)
    else:
        return render_template('list.html', film_list=film_list)


@app.route('/imdb')
def imdb():
    film_list = get_imdb_list()
    if request.args.get('format') == 'json':
        return json_api_response(film_list)
    else:
        return render_template('list.html',
                               film_list=film_list,
                               title='IMDB Top 250',
                               url='http://www.imdb.com/chart/top')


@app.route('/sight-and-sound')
def sight_and_sound():
    film_list = get_bfi_list_with_scores(get_imdb_list())
    if request.args.get('format') == 'json':
        return json_api_response(film_list)
    else:
        return render_template('list.html',
                               film_list=film_list,
                               title='BFI top 11 films of 2012',
                               url='http://www.bfi.org.uk/news-opinion/sight-sound-magazine/polls-surveys/top-11-films-2012')


@app.route('/oscar-best-picture')
def oscar_best_picture():
    film_list = get_oscars_best_picture_list()
    if request.args.get('format') == 'json':
        return json_api_response(film_list)
    else:
        return render_template('list.html',
                               film_list=film_list,
                               title='Oscar Best Picture',
                               url='http://www.oscars.org/awards/academyawards/legacy/best-pictures.html')


@app.route('/oscar-all')
def oscar_all():
    film_list = get_all_oscars_list()
    if request.args.get('format') == 'json':
        json_api_response(film_list)
    else:
        return render_template('list.html',
                               film_list=film_list,
                               title='Oscar All Winners',
                               url='http://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films')


# URLS #########################################################################
app.add_url_rule('/', 'index', index)
app.add_url_rule('/login/', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/logout/', 'logout', logout_view)

if __name__ == '__main__':
    app.debug = True
    # Is this needed? What's the tmp file doing?
    try:
        open('/tmp/app.db')
    except IOError:
        db.create_all()
    app.run()
