from flask import Flask, render_template, request, jsonify, url_for
from data import queries
import math
from dotenv import load_dotenv
import pagination
from util import json_response


load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows')
@app.route('/shows/<int:page>')
def all_shows(page=1):
    number_of_shows = queries.get_show_count()[0]['show_count']
    page_count = math.ceil(number_of_shows/15)
    shown_pages = pagination.check_pages(page, page_count)
    shows = queries.get_shows(page)
    if page <= page_count:
        return render_template('shows.html', shows=shows,
        shown_pages=shown_pages, page_count=page_count,
        page=page)
    else:
        return render_template("error.html")


@app.route('/shows/<order_by>=<order_direction>')
@app.route('/shows/<order_by>=<order_direction>/<int:page>')
def most_rated(page=1, order_by='rating' ,order_direction='DESC'):
    if request.args:
        order_by = list(dict(request.args).keys())[0]
        order_direction = dict(request.args)[order_by]
    number_of_shows = queries.get_show_count()[0]['show_count']
    page_count = math.ceil(number_of_shows/15)
    shown_pages = pagination.check_pages(page, page_count)
    most_rated_shows = queries.get_most_rated_shows(page, order_by, order_direction)
    if page <= page_count:
        return render_template('rated.html', shows=most_rated_shows,
        shown_pages=shown_pages, page_count=page_count,
        page=page, order_by=order_by,
        order_direction=order_direction)
    else:
        return render_template("error.html")


def check_id():
    all_id = queries.get_all_id()
    id_list = [row["id"] for row in all_id]
    return id_list


@app.route('/show/<id>')
def show_details(id):
    if int(id) in check_id():
        show_data = queries.get_show_data(id)[0]
        show_genres = queries.get_genres_from_show(id)
        show_actors = queries.get_show_actors(id)
        seasons = queries.get_seasons(id)
        return render_template('detalis.html', show_data=show_data, 
            show_actors=show_actors, show_genres=show_genres, seasons=seasons)
    else: 
        return render_template("error.html")


def get_actors():
    get_actors= queries.get_100_names()
    actors = [row["name"] for row in get_actors]
    first_names = [actor.split()[0] for actor in actors]
    return first_names


def get_actors_id():
    get_actors= queries.get_100_actors()
    return get_actors


def reunion():
    get_ids = get_actors_id()
    get_first_names = get_actors()
    result = zip(get_ids, get_first_names)
    return list(result)


@app.route('/actors')
def actors():
    actors = reunion()
    return render_template('actors.html', actors = actors)


def main():
    app.run(host='127.0.0.1',
            port=5000,
            debug=True)


if __name__ == '__main__':
    main()
