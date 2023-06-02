from pymongo import MongoClient
import os


class Database:
    @staticmethod
    def db_connection():
        client = MongoClient(os.environ.get("DB_CONNECTION")) 
        db = client['Aufgabe4']
        collection = db['PowerStatistics']
        return collection

    @staticmethod
    def delete_old_logs():
        collection = Database.db_connection()
        count = collection.count_documents({})
        if count > 10000:
            oldest_logs = collection.find().sort('timestamp', 1).limit(count - 10000)
            for log in oldest_logs:
                collection.delete_one({'_id': log['_id']})

    @staticmethod
    def save_to_database(cpu_percent, ram_total, ram_used, timestamp):
        collection = Database.db_connection()
        collection.insert_one({
            'cpu_percent': cpu_percent,
            'ram_total': ram_total,
            'ram_used': ram_used,
            'timestamp': timestamp
        })
