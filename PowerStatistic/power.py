import psutil
from datetime import datetime

class Power():
    def __init__(self):
        self.cpu = psutil.cpu_percent()
        self.ramTotal = psutil.virtual_memory().total
        self.ramInUse = psutil.virtual_memory().used
        self.timestamp = datetime.now()
