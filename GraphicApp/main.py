from pymongo import MongoClient
import matplotlib.pyplot as plt
import os

def plot_power_statistics():
    client = MongoClient("mongodb://localhost:27017/")     #os.environ.get("DB_CONNECTION") TODO: Import the DB Connection function from MainApp/database.py
    db = client['Aufgabe4']
    collection = db['PowerStatistics']
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