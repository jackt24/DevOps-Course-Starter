from flask import Flask, render_template, request
from todo_app.flask_config import Config
from todo_app.data.session_items import *

app = Flask(__name__)
app.config.from_object(Config)

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

if __name__ == '__main__':
    app.run()