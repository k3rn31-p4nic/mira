from datetime import datetime
from flask import current_app
import pymongo

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.created_at = datetime.utcnow()

    @staticmethod
    def get_db():
        client = pymongo.MongoClient(current_app.config['MONGODB_URI'])
        return client.miraflows

    def save(self):
        return self.get_db().users.insert_one(self.__dict__)

    @staticmethod
    def find_by_username(username):
        return User.get_db().users.find_one({"username": username})
