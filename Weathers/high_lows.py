import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as fn:
    reader = csv.reader(fn)
    header_row = next(reader)
    print(header_row)
    for index, header in enumerate(header_row):
        print(index, header)
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, "missind data")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
# picture
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Daily highest and lowest temperatures - 2014')
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatures(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
