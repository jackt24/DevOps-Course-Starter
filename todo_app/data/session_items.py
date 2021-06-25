from flask import session
import requests, os
from dotenv import load_dotenv
from flask.helpers import url_for

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
TOKEN = os.getenv('TOKEN')
BOARD = os.getenv('BOARD')
LIST = os.getenv('LIST')
COMPLETELIST = os.getenv('COMPLETELIST')

def get_items():
    """
    Fetches all todo items from the session.

    Returns:
        list: The list of todo saved items.
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
        items.append({'id': i['id'], 'status': 'ToDo', 'title': i['name'] })
	
    return items

def get_completeitems():
    """
    Fetches all complete items from the session.

    Returns:
        list: The list of completed saved items.
    """
    url = "https://api.trello.com/1/lists/" + COMPLETELIST + "/cards"
    query = {
		'key': SECRET_KEY,
    	'token': TOKEN,
    	}
	
    response = requests.request('GET', url, params=query)
    x=response.json()
    
    completeItems = [ ]
    for i in x:
        completeItems.append({'id': i['id'], 'status': 'Complete', 'title': i['name'] })
	
    return completeItems


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

# Maybe we have to move this to anotehr list - update the list rather than closed. Currently removes from list - Closed deletes
def complete_item(id):
    url = "https://api.trello.com/1/cards/" + id 

    query = {
        'key': SECRET_KEY,
        'token': TOKEN,
        'idList': COMPLETELIST
    }

    headers = {
        "Accept": "application/json"
    }

    response = requests.request('PUT', url, headers=headers, params=query)

    print(response.text)

def delete_item(id):
    url = "https://api.trello.com/1/cards/" + id 

    query = {
        'key': SECRET_KEY,
        'token': TOKEN,
        'closed': 'true'
    }

    headers = {
        "Accept": "application/json"
    }

    response = requests.request('PUT', url, headers=headers, params=query)

    print(response.text)