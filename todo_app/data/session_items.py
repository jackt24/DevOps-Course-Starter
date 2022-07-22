from bson import ObjectId
from flask import session
import requests, os, pymongo
from dotenv import load_dotenv
from flask.helpers import url_for
from todo_app.item import Item
from todo_app.flask_config import Config
from flask import current_app as app


# Returns a list of todo items
def get_items():
    todo_items = []
    mongo_url = app.config['MONGO_URL']
    mongo_db = app.config['MONGO_DB']

    client = pymongo.MongoClient(mongo_url)
    db = client[mongo_db]
    items = db.items
    todo_items = items.find({"status": "ToDo"})

    return todo_items

# Returns a list of complete items 
def get_completeitems():

    complete_items = []
    mongo_url = app.config['MONGO_URL']
    mongo_db = app.config['MONGO_DB']

    client = pymongo.MongoClient(mongo_url)
    db = client[mongo_db]
    items = db.items
    complete_items = items.find({"status": "Complete"})

    return complete_items

# Adds a new item to the todo list with a specified title
def add_item(title):

    newitem = {
        "status":"ToDo",
        "title": title
    }

    mongo_url = app.config['MONGO_URL']
    mongo_db = app.config['MONGO_DB']

    client = pymongo.MongoClient(mongo_url)
    db = client[mongo_db]
    items = db.items
    items.insert_one(newitem).inserted_id

# Move an item from the todo to the complete list
def complete_item(id):

    update = {
        'Status': "Complete"
    }

    mongo_url = app.config['MONGO_URL']
    mongo_db = app.config['MONGO_DB']

    client = pymongo.MongoClient(mongo_url)
    db = client[mongo_db]
    items = db.items

    search = {"_id": ObjectId(id)}

    items.update_one(search, update)

# Remove an item
def delete_item(id):

    mongo_url = app.config['MONGO_URL']
    mongo_db = app.config['MONGO_DB']

    client = pymongo.MongoClient(mongo_url)
    db = client[mongo_db]
    items = db.items

    search = {"_id": ObjectId(id)}

    items.delete_one(search)