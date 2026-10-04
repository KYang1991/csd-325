# Kao Yang
# CSD-325
# Module 4 - High/Low Temperatures
# This program allows the user to view the high or low
# temperatures for Sitka, Alaska in 2018.

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys


# Read the weather data from the CSV file.
filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Continue showing the menu until the user chooses Exit.
while True:

    print("\nSitka Weather Program")
    print("---------------------")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("\nPlease select 1, 2, or 3: ")

    # Display high temperatures.
    if choice == '1':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # Display low temperatures.
    elif choice == '2':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # Exit the program.
    elif choice == '3':
        print("\nThank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()

    # Handle an incorrect menu selection.
    else:
        print("\nInvalid selection. Please choose 1, 2, or 3.")