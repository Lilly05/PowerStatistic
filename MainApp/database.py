from pymongo import MongoClient
import os


class Database:
    def  __init__(self): # connect to database and get collection
        self.collection = self.db_connection() # get collection from database


    @staticmethod
    def db_connection(): # connect to database and return collection
        client = MongoClient(os.environ.get("DB_CONNECTION")) # connect to database
        db = client['Aufgabe4'] # get database
        collection = db['PowerStatistics'] # get collection
        return collection # return collection

    
    def delete_old_logs(self): # delete old logs from database
        count = self.collection.count_documents({}) # get count of logs in database
        if count > 10000:
            oldest_logs = self.collection.find().sort('timestamp', 1).limit(count - 10000) # get oldest logs
            for log in oldest_logs:
                self.collection.delete_one({'_id': log['_id']}) # delete oldest logs

    
    def save_to_database(self, power):
        self.collection.insert_one({
            'cpu_percent': power.cpu_percent,
            'ram_total': power.ram_total,
            'ram_used': power.ram_used,
            'timestamp': power.timestamp
        })
