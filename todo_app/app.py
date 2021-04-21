from flask import Flask, render_template, request
from todo_app.flask_config import Config
from todo_app.data.session_items import *

app = Flask(__name__)
app.config.from_object(Config)

# I added the add functionality to the route rather than a seperate page as this seemed more efficient
@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST': 
		newItemTitle = request.form['text']
		add_item(newItemTitle)
		items = get_items()
		return render_template("index.html", items=items)
	else:
		items = get_items()
		return render_template("index.html", items=items)

@app.route('/complete/<id>', methods=['POST', 'GET'])
def complete(id):
	completeItem = get_item(id)
	completeItem['status'] = 'Complete'
	save_item(completeItem)
	return(id + ' marked as complete')

if __name__ == '__main__':
    app.run()