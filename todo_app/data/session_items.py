from flask import session
import requests, os
from dotenv import load_dotenv
from flask.helpers import url_for
from todo_app.item import Item
from todo_app.flask_config import Config
from flask import current_app as app


# Returns a list of todo items
# So I imagine this is where the mongo stuff needs to come in...
# def get_items2():
    

def get_items():
    url = "https://api.trello.com/1/lists/" + app.config['LIST']+ "/cards"
    query = {
		'key': app.config['TRELLO_KEY'],
        'token': app.config['TOKEN'],
    	}
	
    response = requests.request('GET', url, params=query)
    x=response.json()
    
    items = [ ]
    for i in x:
        items.append(Item(i['id'], 'ToDo', i['name'] ))
	
    return items

# Returns a list of completed items
def get_completeitems():
    url = "https://api.trello.com/1/lists/" + app.config['COMPLETELIST'] + "/cards"
    query = {
	    'key': app.config['TRELLO_KEY'],
        'token': app.config['TOKEN'],
        }
	
    response = requests.request('GET', url, params=query)
    x=response.json()
    
    completeItems = [ ]
    for i in x:
        completeItems.append(Item(i['id'], 'Complete', i['name'] ))
	
    return completeItems

# Adds a new item to the todo list with a specified title
def add_item(title):

    url = "https://api.trello.com/1/cards"

    query = {
        'key': app.config['TRELLO_KEY'],
        'token': app.config['TOKEN'],
        'idList': app.config['LIST'],
        'name': title
    }

    response = requests.request(
        'POST',
        url,
        params=query
    )

    # print(response.text)

# Move an item from the todo to the complete list
def complete_item(id):
    url = "https://api.trello.com/1/cards/" + id 

    query = {
        'key': app.config['TRELLO_KEY'],
        'token': app.config['TOKEN'],
        'idList': app.config['COMPLETELIST']
    }

    headers = {
        "Accept": "application/json"
    }

    response = requests.request('PUT', url, headers=headers, params=query)

    # print(response.text)

# Remove an item
def delete_item(id):
    url = "https://api.trello.com/1/cards/" + id 

    query = {
        'key': app.config['TRELLO_KEY'],
        'token': app.config['TOKEN'],
        'closed': 'true'
    }

    headers = {
        "Accept": "application/json"
    }

    response = requests.request('PUT', url, headers=headers, params=query)

    # print(response.text)