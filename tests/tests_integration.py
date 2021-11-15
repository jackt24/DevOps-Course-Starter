from unittest import mock
from todo_app.data.session_items import BOARD
from unittest.mock import patch, Mock
import pytest
from dotenv import load_dotenv, find_dotenv

from todo_app.app import create_app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


patch('requests.request')
def test_index_page(to_patch, client):
    to_patch.side_effect = mock_requests_request

    mock_requests_request.side_effect = mock_get_lists

    response = client.get('/')

    response_html = response.data.decode()
    print(response_html)
    assert 'ToDo Items' in response_html
    
    # Rest of your test here

def mock_requests_request(method, url, params):
    if method == 'GET' and url == f'https://api.trello.com/1/lists/" + os.getenv('LIST') + "/cards':
        response = Mock()
        response.json.return_value = [{"id": "123", "name": "My Test Task"}]
        return response

    # TODO: Mock out getting cards from the "Complete" list

    raise Exception(f'Call to {method} {url} is not mocked!')



# @patch('requests.get')
# def test_index_page(mock_get_requests, client):
#  # Replace call to requests.get(url) with our ownunction
#     mock_get_requests.side_effect = mock_get_lists

#     response = client.get('/')

#     response_html = response.data.decode()
#     print(response_html)
#     assert 'ToDo Items' in response_html

# def mock_get_lists(url, params):
#     if url == f'https://api.trello.com/1/boards/{BOARD}/lists':
#         response = mock()
 
#     response_html = response.data.decode()
#  # sample_trello_lists_response should point to some test response data
#     response.json.return_value = response_html
#     return response
#     return None