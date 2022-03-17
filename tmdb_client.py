import requests
from flask import Flask
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNzE0YzIxMGFmNGJmYzZlYjBjZjI3YjhiZjgyN2M3OSIsInN1YiI6IjYxZmMwMjBkN2E5N2FiMDBlNDY2MjFmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.77qRfdx5C9SnDqNKDE7JrPcIv8Gp9gw5LeMgN0xKq5I"

app = Flask(__name__)

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    data_list = data["results"]
    shuffle_data = random.shuffle(data_list)
    print(shuffle_data)
    return data["results"][:how_many]
    

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_random_picture(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)