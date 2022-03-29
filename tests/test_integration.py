from unittest import mock
from unittest.mock import patch, Mock
import pytest
from dotenv import load_dotenv, find_dotenv
import os

from todo_app.app import create_app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    try:
        file_path = find_dotenv('.env.test')
        load_dotenv(file_path, override=True)
    except:
        pass
    
    # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


@patch('requests.request')
def test_index_page(to_patch, client):
    to_patch.side_effect = mock_requests_request

    response = client.get('/')

    response_html = response.data.decode()
    assert 'ToDo Items' in response_html
    assert 'My Complete Task' in response_html

def mock_requests_request(method, url, params):
    if method == 'GET' and url == f'https://api.trello.com/1/lists/' + os.getenv('LIST') + '/cards':
        response = Mock()
        response.json.return_value = [{"id": "123", "name": "My Test Task"}]
        return response

    if method == 'GET' and url == 'https://api.trello.com/1/lists/' + os.getenv('COMPLETELIST') + '/cards':
        response = Mock()
        response.json.return_value = [{"id": "456", "name": "My Complete Task"}]
        return response

    raise Exception(f'Call to {method} {url} is not mocked!')

