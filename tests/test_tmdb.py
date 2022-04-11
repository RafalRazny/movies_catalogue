import pytest
import tmdb_client
from unittest.mock import Mock
import requests

def test_get_sinlgle_movie(monkeypatch):
    mock_movie = ['568124']
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    single_movie = tmdb_client.get_single_movie(movie_id='568124')
    assert mock_movie == single_movie

def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    excpected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert excpected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

def test_get_sinlgle_movie(monkeypatch):
    mock_movie = ['568124']
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    single_movie = tmdb_client.get_single_movie(movie_id='568124')
    assert mock_movie == single_movie

def test_get_single_movie_cast(monkeypatch):
    mock_cast = ['680']
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_cast
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    single_cast = tmdb_client.get_single_movie_cast(movie_id='680')
    assert mock_cast == single_cast
