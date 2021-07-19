import os


class Config:

    def __init__(self):
            self.TRELLO_BASE_URL = 'https://api.trello.com/1'
            self.TRELLO_KEY = os.environ.get('TRELLO_KEY')
            self.TOKEN = os.environ.get('TOKEN')
            self.BOARD = os.environ.get('BOARD')
            self.LIST = os.environ.get('LIST')
            self.BOARD = os.environ.get('COMPLETELIST')

    # """Base configuration variables."""
    # TRELLO_KEY = os.environ.get('TRELLO_KEY')
    # if not TRELLO_KEY:
    #     raise ValueError("No TRELLO_KEY set for Flask application. Did you follow the setup instructions?")
