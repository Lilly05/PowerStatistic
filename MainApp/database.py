from pymongo import MongoClient
import os


class Database:
    def  __init__(self):
        self.collection = self.db_connection()


    @staticmethod
    def db_connection():
        client = MongoClient(os.environ.get("DB_CONNECTION")) 
        db = client['Aufgabe4']
        collection = db['PowerStatistics']
        return collection

    
    def delete_old_logs(self):
        count = self.collection.count_documents({})
        if count > 10000:
            oldest_logs = self.collection.find().sort('timestamp', 1).limit(count - 10000)
            for log in oldest_logs:
                self.collection.delete_one({'_id': log['_id']})

    
    def save_to_database(self, power):
        self.collection.insert_one({
            'cpu_percent': power.cpu_percent,
            'ram_total': power.ram_total,
            'ram_used': power.ram_used,
            'timestamp': power.timestamp
        })
