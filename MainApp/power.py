from pymongo import MongoClient
import psutil
import time

class Power:
    def __init__(self, cpu_percent, ram_total, ram_used, _id = None, timestamp=None):
        if(_id is not None):
            self._id = _id
        self.cpu_percent = cpu_percent
        self.ram_total = ram_total
        self.ram_used = ram_used
        if timestamp is None:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

    def update_usage(self):
        self.cpu_percent = psutil.cpu_percent()
        mem_info = psutil.virtual_memory()
        self.ram_total = mem_info.total
        self.ram_used = mem_info.used