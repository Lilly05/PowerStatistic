from pymongo import MongoClient
import psutil
import time

class Power:
    def __init__(self, timestamp=None):
        self.cpu_percent = None
        self.ram_total = None
        self.ram_used = None
        if timestamp is None:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

    def update_usage(self):
        self.cpu_percent = psutil.cpu_percent()
        mem_info = psutil.virtual_memory()
        self.ram_total = mem_info.total
        self.ram_used = mem_info.used