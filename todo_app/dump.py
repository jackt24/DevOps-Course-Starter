# @@ -0,0 +1,65 @@
# from os import name
# from flask import Flask, render_template, request
# # from flask_config import Config
# from data.session_items import get_items, add_item, save_item, get_item
# from requests import *
# import json


# app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return 'Web App with Python Flask!'

# # app.config.from_object(Config)

# SECRET_KEY = '67c80a86e3b5e5128344a646e1805ea5'
# TOKEN = '8f4ea03ffc2cda30041aa7c6b87cd5ddf05f76409cf37967ad304e07d01485c5'
# BOARD = '60ace9c7e035d1378036b868'

# # @app.route('/trello', methods=['POST', 'GET'])
# # def displayItems():
# # 	resp = []
# # 	resp2 = []
# # 	int = 0
# # 	url = "https://api.trello.com/1/boards/"+BOARD+"/cards?key="+SECRET_KEY+"&token="+TOKEN+""
# # 	resp = get(url).json()
# # 	for item in resp:
# # 		resp2+=resp[int]
# # 		int


# # 	# resp2= json.loads(resp)


# # 	# desc = resp.get('id').get('desc')
# # 	# idShort = []
# # 	# resp2 = get(url)
# # 	# resp += [resp.json()]
# # 	# id = resp.get('name')
# # 	# resp += [b_resp.json()]
# # 	return str(resp2)
# # 	# return str(resp)

# # I added add functionality to the route rather than a seperate page as this seemed more efficient
# @app.route('/', methods=['POST', 'GET'])
# def index():
# 	if request.method == 'POST': 
# 		newItemTitle = request.form['text']
# 		add_item(newItemTitle)
# 		items = get_items()
# 		return render_template("index.html", items=items)
# 	else:
# 		items = get_items()
# 		return render_template("index.html", items=items)

# @app.route('/complete/<id>', methods=['POST', 'GET'])
# def complete(id):
# 	completeItem = get_item(id)
# 	completeItem['status'] = 'Complete'
# 	save_item(completeItem)
# 	return(id + ' marked as complete')

# if __name__ == '__main__':
#     app.run()