from dotenv import load_dotenv, find_dotenv
from todo_app import app
import pytest
import os
import requests

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def stub(url, params={}):
    test_board_id = os.environ.get('BOARD_ID')
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    Expected_Trello_url = f"https://api.trello.com/1/boards/{test_board_id}/lists?cards=open&key={key}&token={token}"

    if url == Expected_Trello_url :
        fake_response_data = [{
            'id': '123abc',
            'name': 'To do',
            'cards': [{'id': '456', 'name': 'Test card'}]
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    # Replace requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', stub)

    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
