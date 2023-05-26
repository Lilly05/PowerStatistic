from pymongo import MongoClient
import os

# Linux: export CONNECTION_STRING=""
# printenv CONNECTION_STRING

# Windows: set CONNECTION_STRING="" | $CONNECTION_STRING=""
# echo CONNECTION_STRING

class Database:
    def __init__(self):
        self.connectToDatabase()
        self.db = self.getDatabase()
        self.collection = self.getCollection(self.db)
    
    def connectToDatabase():
        client = MongoClient(os.environ.get("CONNECTION_STRING"))

    def getDatabase():
        return MongoClient['Aufgabe4']

    def getCollection(db):
        return db['PowerStatistics']
