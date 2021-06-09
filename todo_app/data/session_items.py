from ast import Index
from flask import session
from flask.helpers import url_for
import requests

SECRET_KEY = '67c80a86e3b5e5128344a646e1805ea5'
TOKEN = '8f4ea03ffc2cda30041aa7c6b87cd5ddf05f76409cf37967ad304e07d01485c5'
BOARD = '60ace9c7e035d1378036b868'
LIST = '60acf2c006fcce49c3cdc33a'

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    url = "https://api.trello.com/1/lists/" + LIST + "/cards"
    query = {
		'key': SECRET_KEY,
    	'token': TOKEN,
    	}
	
    response = requests.request('GET', url, params=query)
    x=response.json()
    
    items = [ ]
    for i in x:
        items.append({'id': i['id'], 'status': 'Not Started', 'title': i['name'] })
	
    return items

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    # items = get_items()

    url = "https://api.trello.com/1/cards"

    query = {
        'key': SECRET_KEY,
        'token': TOKEN,
        'idList': LIST,
        'name': title
    }

    response = requests.request(
        'POST',
        url,
        params=query
    )

    print(response.text)

    # # Determine the ID for the item based on that of the previously added item
    # id = items[-1]['id'] + 1 if items else 0

    # item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # # Add the item to the list
    # items.append(item)
    # session['items'] = items

    # return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items
    
    return item

def complete_item(id):
    return url_for(Index)