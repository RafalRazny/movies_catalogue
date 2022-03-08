import tmdb_client
import main
from unittest.mock import Mock
import requests
from main import app
import pytest

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNzE0YzIxMGFmNGJmYzZlYjBjZjI3YjhiZjgyN2M3OSIsInN1YiI6IjYxZmMwMjBkN2E5N2FiMDBlNDY2MjFmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.77qRfdx5C9SnDqNKDE7JrPcIv8Gp9gw5LeMgN0xKq5I"
headers =  {"Authorization": f"Bearer {API_TOKEN}"
    }
def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    excpected_default_size = 'w342'
    poster_url = main.tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert excpected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type='popular')
   assert movies_list == mock_movies_list

def test_get_sinlgle_movie(monkeypatch):
    mock_movie = ['568124']
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    single_movie = tmdb_client.get_single_movie(movie_id='568124')
    assert mock_movie == single_movie

def call_tmdb_api_for_credits(endpoint):
    full_url = f"https://api.themovie.org/3/{endpoint}/credits"
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_single_movie_cast(movie_id):
    return call_tmdb_api_for_credits(f'{movie_id}/credits')

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("main.tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')

@pytest.mark.parametrize('how_many, list_type',(
  ('8', '4'), ('popular', 'top_rated')))

def test_get_movies(monkeypatch, list_type, how_many):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("main.tmdb_client.call_tmdb_api", api_mock)

    with app.test_client(list_type, how_many) as client:
       response = client.get(f'/movies/{list_type}{how_many}')
       single_movie = tmdb_client.get_movies(list_type=list_type, how_many=how_many)
       assert response.get_movies == single_movie
       api_mock.assert_called_once_with('movie/popular[:4]')