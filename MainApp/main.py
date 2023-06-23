import time
from database import Database
from power import Power

db = Database()

while True:
    db.save_to_database(Power())
    db.delete_old_logs()
    time.sleep(1)