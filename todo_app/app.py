from flask import Flask, render_template
# from data.session_items as myData
from todo_app.flask_config import Config
from todo_app.data.session_items import *
# from data import session_items

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/todo/list')
def list():
	items = get_items()
	return render_template("index.html", items=items)

if __name__ == '__main__':
    app.run()
