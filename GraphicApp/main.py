import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MainApp.database import Database
import matplotlib.pyplot as plt


def plot_power_statistics():
    collection = Database.db_connection()
    logs = collection.find().sort('timestamp', 1)

    timestamps = []
    ram_totals = []
    ram_useds = []
    cpu_percentages = []

    for log in logs:
        timestamps.append(log['timestamp'])
        ram_totals.append(log['ram_total'])
        ram_useds.append(log['ram_used'])
        cpu_percentages.append(log['cpu_percent'])

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(timestamps, ram_totals, label='RAM Total')
    ax1.plot(timestamps, ram_useds, label='RAM Used')
    ax1.set_ylabel('RAM Usage')
    ax1.legend()

    ax2.plot(timestamps, cpu_percentages, label='CPU Percent', color='red')
    ax2.set_xlabel('Timestamp')
    ax2.set_ylabel('CPU Usage')
    ax2.legend()

    plt.show()


plot_power_statistics()