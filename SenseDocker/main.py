import csv
import time
import matplotlib.pyplot as plt
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

plt.ion()
fig, ax = plt.subplots()

def read_data_from_csv(csv_file):
    times, temps, humidities = [], [], []
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                time_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                times.append(time_obj)
                temps.append(float(row[1]))
                humidities.append(float(row[2]))
    except FileNotFoundError:
        print("CSV file not found. Starting new one.")
    return times, temps, humidities

csv_file = '/home/pi/Documents/SenseDocker/database.csv'

try:
    times, temps, humidities = read_data_from_csv(csv_file)
    
    while True:
        temp = round(sense.get_temperature(), 1)
        humidity = round(sense.get_humidity(), 1)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{current_time}, {temp}, {humidity}")

        msg = "T = %s, H = %s%%" % (temp, humidity) 
        sense.show_message(msg, scroll_speed=0.1)  

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Time", "Temperature", "Humidity"])
            writer.writerow([current_time, temp, humidity])

        times, temps, humidities = read_data_from_csv(csv_file)
        ax.clear()
        ax.set_xlabel('Time')
        ax.set_ylabel('Hum/ Temp')
        ax.set_title('Temperature vs Humidity over Time')
        ax.plot(times, humidities, 'go-', label='Humidity')
        ax.plot(times, temps, 'ro-', label='Temperature')
        plt.xticks(rotation=45)
        ax.legend()
        plt.draw()
        plt.pause(1)

        time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

finally:
    plt.ioff()
    plt.show()


