import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MainApp.database import Database
from MainApp.power import Power
import matplotlib.pyplot as plt
from datetime import datetime



def plot_power_statistics():
    db = Database() # connect to database
    collection = db.collection # get collection

    powers = []
    for power_data in collection.find(): # get all data from collection
        powers.append(Power(**power_data)) # create Power object from data

    timestamps = [power.timestamp for power in powers] # get timestamps from powers
    ram_totals = [power.ram_total for power in powers] # get ram totals from powers
    ram_useds = [power.ram_used for power in powers] # get ram useds from powers
    cpu_percentages = [power.cpu_percent for power in powers] # get cpu percentages from powers
    print(timestamps)
    time_strings = [datetime.fromtimestamp(timestamp).strftime("%H:%M:%S") for timestamp in timestamps]
    date_strings = [datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d") for timestamp in timestamps]

    print(time_strings)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True) # create figure with 2 subplots

    ax1.plot(time_strings, ram_totals, label='RAM Total') # plot ram totals
    ax1.plot(time_strings, ram_useds, label='RAM Used') # plot ram useds

    ax2.plot(time_strings, cpu_percentages, label='CPU Percent', color='red') # plot cpu percentages

    ax1.set_ylabel('RAM Usage') # set y label for subplot 1
    ax1.legend() # show legend for subplot 1

    ax2.set_xlabel('Datum und Zeit: ' + date_strings[0]) # set x label for subplot 2
    ax2.set_ylabel('CPU Usage') # set y label for subplot 2
    ax2.legend() # show legend for subplot 2

    plt.xticks(rotation=90)  # Rotate x-axis labels vertically

    plt.show() # show plot


plot_power_statistics() # plot power statistics
