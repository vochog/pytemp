import csv
import time
from datetime import datetime


#sample data (8 lines each)
temperature = [18, 22, 25, 19, 21, 23, 27, 28]
power = [1500, 1600, 1700, 1550, 1650, 1750, 1800, 1900]
occupancy = [1, 0, 1, 1, 0, 1, 0, 1]

# File names
temp_file = 'temperature.csv'
power_file = 'power.csv'
occupancy_file = 'occupancy.csv'

# Initialize index
index = 0
data_len = len(temperature)

# write header if needed
# def init_csv(file_name, header):
#     try:
#         with open(file_name, 'x', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(header)
#     except FileExistsError:
#         pass # File already exists, no action needed

# init_csv(temp_file, ['timestamp', 'temperature'])
# init_csv(power_file, ['timestamp', 'power'])
# init_csv(occupancy_file, ['timestamp', 'occupancy'])

# Loop forever
while True:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get 
    temp = temperature[index]
    pow = power[index]
    occ = occupancy[index]

    # Append data to CSV files
    with open(temp_file, 'a', newline='') as file:
        csv.writer(file).writerow([now, temp])
    with open(power_file, 'a', newline='') as file:
        csv.writer(file).writerow([now, pow])
    with open(occupancy_file, 'a', newline='') as file:
        csv.writer(file).writerow([now, occ])

    print(f"Logged entry #{index + 1} at {now}:")

    # Update index
    index = ( index + 1) % data_len

    # Sleep for 60 second
    time.sleep(60)