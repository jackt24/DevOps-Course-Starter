from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import *
from todo_app import item

app = Flask(__name__)
app.config.from_object(Config)

# Populate Lists and add items 
@app.route('/',methods=['POST', 'GET'])
def index():
	if request.method == 'POST': 
		newItemTitle = request.form['text']
		add_item(newItemTitle)
		items = get_items()
		complete_items = get_completeitems()
		return render_template("index.html", items=items, complete_items=complete_items)
	else:
		items = get_items()
		complete_items = get_completeitems()
		return render_template("index.html", items=items, complete_items=complete_items)

# Move an item from the todo list to the complete list
@app.route('/complete/<id>')
def complete(id):
	complete_item(id)
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)