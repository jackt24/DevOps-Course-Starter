from unittest import mock
from todo_app.data.session_items import BOARD
from unittest.mock import patch, Mock
from flask import app
import pytest
import requests, os
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

@patch('requests.get')
def test_index_page(mock_get_requests, client):
 # Replace call to requests.get(url) with our ownunction
    mock_get_requests.side_effect = mock_get_lists

    response = client.get('/')

def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/{BOARD}/lists':
        response = mock()
 
    response_html = response.data.decode()
 # sample_trello_lists_response should point to some test response data
    response.json.return_value = response_html
    return response
    return None

    