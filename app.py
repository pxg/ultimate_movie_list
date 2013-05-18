import json
import decimal
from flask import Flask, Response, render_template, request
from combine_lists import *
app = Flask(__name__)


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


@app.route('/')
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


if __name__ == '__main__':
    app.debug = True
    app.run()
