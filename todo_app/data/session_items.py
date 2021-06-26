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

# Returns a list of todo items
def get_items():
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

# Returns a list of completed items
def get_completeitems():
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

# Gets an item from the list based on ID
def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

# Adds a new item to the todo list with a specified title
def add_item(title):

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

# Redundant?
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

# Move an item from the todo to the complete list
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

# Remove an item
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