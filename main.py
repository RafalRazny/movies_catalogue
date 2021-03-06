from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get("list_type", "popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    list_types = ("popular", "top_rated", "upcoming", "now_playing")
    return render_template("homepage.html", movies=movies, list_types=list_types, selected_list=selected_list)

#def get_movie_info():
    movies_2 = tmdb_client.get_popular_movies()["results"][:8]
    results = {}
    for titles_dict in movies_2:
        keys = ["title", "poster_path"]
        dict2 = {x:titles_dict[x] for x in keys}
        results[dict2["title"]] = dict2
    return results

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url} 

@app.context_processor
def utility_processor():
    def details_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"details_image_url": details_image_url}

@app.context_processor
def utility_processor():
    def cast_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"cast_image_url": cast_image_url}

@app.context_processor
def utility_processor():
    def picture_random_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"picture_random_url": picture_random_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    dict_raw = tmdb_client.get_single_movie_cast(movie_id)["cast"][:8]
    collection_photos = tmdb_client.get_random_picture(movie_id)["backdrops"]
    some_photo = random.choice(collection_photos)
    return render_template("movie_details.html", movie=details, casts=dict_raw, photos=some_photo)

if __name__ == '__main__':
    app.run(debug=True)