import os
from threading import Thread
import dotenv
import pytest
from selenium import webdriver
from dotenv import load_dotenv
import requests

from todo_app.flask_config import Config
from todo_app.app import create_app



@pytest.fixture(scope="module")
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    
    with webdriver.Chrome(options=opts) as driver:
        yield driver

# Id organisation board on trello - create default id
#
def create_trello_board():
    config = Config()
    response = requests.post(
        url=f'{config.TRELLO_BASE_URL}/boards',
        params={
            'key': config.TRELLO_KEY,
            'token': config.TOKEN,
            'name': 'Selenium Test Board'
        }
    )
    print (response.text)
    return response.json()['id']

def set_list_ids():
    config = Config()
    response = requests.get(
        url=f'{config.TRELLO_BASE_URL}/boards/{config.BOARD}/lists',
        params={
            'key': config.TRELLO_KEY,
            'token': config.TOKEN,
        }
    )
    lists = response.json()
    os.environ['LIST'] = lists[0]["id"]
    os.environ['COMPLETELIST'] = lists[2]["id"]




def delete_trello_board(board_id):
    config = Config()
    requests.delete(
        url=f'{config.TRELLO_BASE_URL}/boards/{board_id}',
        params={
            'key': config.TRELLO_KEY,
            'token': config.TOKEN,
        }
    )

@pytest.fixture(scope='module')
def app_with_temp_board():
    # Load variables?
    try:
        load_dotenv(override=True)
    except:
        pass

    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['BOARD'] = board_id
    
    set_list_ids()
 
    # construct the new application
    application = create_app()
    
    # start the app in its own thread.
    thread = Thread(target=lambda:
    application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
 
    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'
