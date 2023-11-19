from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models import Anime
from app.anime_util import fetch_anime_info

@app.route('/')
@app.route('/index')
def index():
    animes = Anime.query.all()
    return render_template('index.html', animes=animes)


@app.route('/anime/<name>')
def anime(name):
    try:
        anime = Anime.query.filter_by(name=name).first_or_404()
    except Exception as e:
        return str(e), 500
    return render_template('anime.html', anime=anime)


@app.route('/anime/<name>/delete', methods=['POST'])
def delete_anime(name):
    anime = Anime.query.filter_by(name=name).first_or_404()
    db.session.delete(anime)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(anime.name))
    return redirect(url_for('index'))


@app.route('/search', methods=['GET', 'POST'])
def search_anime_by_name():
    if request.method == "POST":
        anime_name = request.form.get("anime_name")
        search_result = fetch_anime_info(anime_name)
        # Debugging: Print the API response
        print(search_result)
        return render_template("search_results.html", result=search_result['data']['Media']) # Mind the lowercase 'data'
    return render_template("search_result.html")


@app.route('/anime/create', methods=['GET', 'POST'])
def create_anime():
    if request.method == 'POST':
        name = request.form['name']
        if not name.strip():
            return "Name cannot be empty. Please enter a valid anime name."
        new_anime = Anime(name=name.strip())  # strip leading/trailing spaces
        try:
            db.session.add(new_anime)
            db.session.commit()
            return redirect(url_for('anime', name=new_anime.name))
            # return redirect(url_for('index'))
        except Exception as e:
            print(e)
            return "There was a problem adding new anime, yo."

    else:
        return render_template('create.html')


@app.route('/anime/<name>/edit', methods=['GET', 'POST'])
def edit_anime(name):
    anime = Anime.query.filter_by(name=name).first_or_404()
    if request.method == 'POST':
        anime.name = request.form['name']
        db.session.commit()
        flash('"{}" was successfully updated!'.format(anime.name))
        return redirect(url_for('anime', name=anime.name))
    return render_template('edit.html', anime=anime)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Import app after routes defined
from app import app
