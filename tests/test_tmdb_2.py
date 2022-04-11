import pytest
from main import app

@pytest.mark.parametrize('list_type',[
  ('popular', 'top_rated', 'upcoming','now_playing')])

def test_homepage(list_type):
   homepage_path = f'/{list_type}'
   
   with app.test_client() as client:
       response = client.get('/{list_type}')
       assert response.status_code == 200
       assert homepage_path == response
