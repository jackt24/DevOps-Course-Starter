import os


class Config:

    def __init__(self):
            self.MONGO_URL = os.getenv('MONGO_URL')
            self.MONGO_DB = os.getenv('MONGO_DB')