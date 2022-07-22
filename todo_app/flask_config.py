import os


class Config:

    def __init__(self):
            # self.TRELLO_BASE_URL = 'https://api.trello.com/1'
            self.MONGO_URL = os.getenv('MONGO_URL')
            self.MONGO_DB = os.getenv('MONGO_DB')
            self.TRELLO_KEY = os.environ.get('TRELLO_KEY')
            self.TOKEN = os.environ.get('TOKEN')
            self.BOARD = os.environ.get('BOARD')
            self.LIST = os.environ.get('LIST')
            self.COMPLETELIST = os.environ.get('COMPLETELIST')