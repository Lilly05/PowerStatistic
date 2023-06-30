import psutil
import time

class Power:
    def __init__(self, cpu_percent=None, ram_total=None, ram_used=None, _id=None, timestamp=None):
        self._id = _id if _id is not None else None # _id is None if object is not saved in database
        self.cpu_percent = cpu_percent if cpu_percent is not None else psutil.cpu_percent() # get cpu percent if not given
        self.ram_total = ram_total if ram_total is not None else psutil.virtual_memory().total # get ram total if not given
        self.ram_used = ram_used if ram_used is not None else psutil.virtual_memory().used # get ram used if not given
        self.timestamp = timestamp if timestamp is not None else time.time() # get timestamp if not given