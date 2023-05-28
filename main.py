import time
from database import Database
from power import Power

while True:
    power = Power()
    power.update_usage()
    Database.save_to_database(power.cpu_percent, power.ram_total, power.ram_used, power.timestamp)
    Database.delete_old_logs()
    time.sleep(1)