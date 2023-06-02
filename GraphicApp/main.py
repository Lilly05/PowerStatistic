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
        power = Power(**power_data)
        powers.append(power)

    timestamps = []
    ram_totals = []
    ram_useds = []
    cpu_percentages = []

    for power in powers:
        timestamps.append(power.timestamp)
        ram_totals.append(power.ram_total)
        ram_useds.append(power.ram_used)
        cpu_percentages.append(power.cpu_percent)

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
