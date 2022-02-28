import tmdb_client
import json
import pytest
from unittest.mock import Mock

def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    excpected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert excpected_default_size in poster_url
    #assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.request.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type='popular')
   assert movies_list == mock_movies_list

def test_get_sinlgle_movie(monkeypatch):
    mock_movie = ['Movie 1']
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.request.get", request_mock)
    single_movie = tmdb_client.get_single_movie(movie_id='47669')
    assert mock_movie == single_movie

