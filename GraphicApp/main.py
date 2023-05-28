from pymongo import MongoClient
import matplotlib.pyplot as plt

def plot_power_statistics():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['Aufgabe4']
    collection = db['PowerStatistics']
    logs = collection.find().sort('timestamp', 1)

    timestamps = []
    cpu_percentages = []
    ram_totals = []
    ram_useds = []

    for log in logs:
        timestamps.append(log['timestamp'])
        cpu_percentages.append(log['cpu_percent'])
        ram_totals.append(log['ram_total'])
        ram_useds.append(log['ram_used'])

    plt.plot(timestamps, cpu_percentages, label='CPU Percent')
    plt.plot(timestamps, ram_totals, label='RAM Total')
    plt.plot(timestamps, ram_useds, label='RAM Used')

    plt.xlabel('Timestamp')
    plt.ylabel('Usage')
    plt.legend()
    plt.show()

plot_power_statistics()