import time
from database import Database
from power import Power

db = Database() # connect to database

while True: # loop forever
    db.save_to_database(Power()) # save power to database
    db.delete_old_logs() # delete old logs from database
    time.sleep(1) # wait 1 second