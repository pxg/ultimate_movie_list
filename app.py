import json
import decimal
from flask import Flask, Response, render_template, jsonify
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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ultimate-list')
def ultimate_list():
    film_list = get_ultimate_movie_list()
    return render_template('list.html', film_list=film_list)

#TODO: Link to all Oscar winners

@app.route('/ultimate-list/json')
def ultimate_list_api():
    film_list = get_ultimate_movie_list()
    return Response(json.dumps(film_list, cls=DecimalEncoder),
                    mimetype='application/json')


@app.route('/imdb')
def imdb():
    film_list = get_imdb_list()
    return render_template('list.html',
                           film_list=film_list,
                           title='IMDB Top 250',
                           url='http://www.imdb.com/chart/top')


@app.route('/imdb/json')
def imdb_api():
    film_list = get_imdb_list()
    return Response(json.dumps(film_list, cls=DecimalEncoder),
                    mimetype='application/json')


@app.route('/sight-and-sound')
def sight_and_sound():
    film_list = get_bfi_list_with_scores(get_imdb_list())
    return render_template('list.html',
                           film_list=film_list,
                           title='BFI top 11 films of 2012',
                           url='http://www.bfi.org.uk/news-opinion/sight-sound-magazine/polls-surveys/top-11-films-2012')


@app.route('/sight-and-sound/json')
def sight_and_sound_api():
    film_list = get_bfi_list_with_scores(get_imdb_list())
    return Response(json.dumps(film_list, cls=DecimalEncoder),
                    mimetype='application/json')


@app.route('/oscar-best-picture')
def oscar_best_picture():
    film_list = get_oscars_best_picture_list()
    return render_template('list.html',
                           film_list=film_list,
                           title='Oscar Best Picture',
                           url='http://www.oscars.org/awards/academyawards/legacy/best-pictures.html')


@app.route('/oscar-best-picture/json')
def oscar_best_picture_api():
    film_list = get_oscars_best_picture_list()
    return Response(json.dumps(film_list, cls=DecimalEncoder),
                    mimetype='application/json')


if __name__ == '__main__':
    app.debug = True
    app.run()
