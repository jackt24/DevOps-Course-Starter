from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import *
from todo_app import item

app = Flask(__name__)
app.config.from_object(Config)

# Populate lists and add items 
@app.route('/',methods=['POST', 'GET'])
def index():
	items = get_items()
	complete_items = get_completeitems()
	return render_template("index.html", items=items, complete_items=complete_items)

# Add an item to the to do list
@app.route('/add', methods=['POST', 'GET'])
def add():
	newItemTitle = request.form['text']
	add_item(newItemTitle)
	return redirect(url_for('index'))

# Move an item from the todo list to the complete list
@app.route('/complete/<id>')
def complete(id):
	complete_item(id)
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)