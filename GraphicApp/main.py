import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MainApp.database import Database
from MainApp.power import Power
import matplotlib.pyplot as plt


def plot_power_statistics():
    db = Database()
    collection = db.collection

    powers = []
    for power_data in collection.find():
        powers.append(Power(**power_data))

    timestamps = [power.timestamp for power in powers]
    ram_totals = [power.ram_total for power in powers]
    ram_useds = [power.ram_used for power in powers]
    cpu_percentages = [power.cpu_percent for power in powers]

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(timestamps, ram_totals, label='RAM Total')
    ax1.plot(timestamps, ram_useds, label='RAM Used')

    ax2.plot(timestamps, cpu_percentages, label='CPU Percent', color='red')

    ax1.set_ylabel('RAM Usage')
    ax1.legend()

    ax2.set_xlabel('Timestamp')
    ax2.set_ylabel('CPU Usage')
    ax2.legend()

    plt.show()


plot_power_statistics()
