from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import *

app = Flask(__name__)
app.config.from_object(Config)

# Gets all lists from the board
# @app.route('/trello')
# def displayItems():
# 	url = "https://api.trello.com/1/lists/" + LIST + "/cards"
# 	query = {
# 		'key': SECRET_KEY,
#     	'token': TOKEN,
#     	}
	
# 	print("")
# 	response = requests.request('GET', url, params=query)
# 	x=response.json()
    
# 	items = [ ]
# 	for i in x:
# 		items.append({'id': i['id'], 'status': 'Not Started', 'title': i['name'] })
	
# 	return items

# I added add functionality to the route rather than a seperate page as this seemed more efficient
@app.route('/',methods=['POST', 'GET'])
def index():
	if request.method == 'POST': 
		newItemTitle = request.form['text']
		add_item(newItemTitle)
		items = get_items()
		return render_template("index.html", items=items)
	else:
		items = get_items()
		return render_template("index.html", items=items)

@app.route('/complete/<id>')
def complete(id):
	complete_item(id)
	return redirect(url_for('index'))
	# if request.method == 'PUT':
	# 	complete_item(id)
	# 	return redirect(url_for('index'))
	# else:
	# 	return redirect(url_for('index'))

# @app.route('/lol', methods=['POST', 'GET'])
# def lol():
# 	return print("hello world")

if __name__ == '__main__':
    app.run(debug=True)