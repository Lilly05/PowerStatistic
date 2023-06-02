import time
from database import Database
from power import Power

db = Database()
power = Power()

while True:
    power.update_usage()
    db.save_to_database(power.cpu_percent, power.ram_total, power.ram_used, power.timestamp)
    db.delete_old_logs()
    time.sleep(1)