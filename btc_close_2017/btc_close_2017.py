from __future__ import(absolute_import, division,
                       unicode_literals, print_function)
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import json
#import requests
import pygal
import math
from itertools import groupby

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response = urlopen(json_url)
req = response.read()
#req = requests.get(json_url)
with open('btc_close_2017_urllib.json', 'wb') as file:
    file.write(req)
    # file.write(req.text)
file_urllib = json.loads(req)
#file_requests = req.json()
# print(file_urllib)
filename = "btc_close_2017.json"
with open(filename) as afile:
    btc_data = json.load(afile)
dates = []
months = []
weeks = []
weekdays = []
closes = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))
    # print("{} is month {} week {}, {}, the close price is {} RMB".format(
    #     date, month, week, weekday, close))

# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = 'Close_Prices(¥)'
# line_chart.x_labels = dates
# N = 20
# line_chart.x_labels_major = dates[::N]
# closes_log = [math.log10(_) for _ in closes]
# line_chart.add('Close_SPrice', closes_log)
# line_chart.render_to_file('closes_log10.svg')
# line_chart.render_to_file('closes.svg')


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([str(x), sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


# 绘制收盘价月日均价
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], closes[:idx_month], "closes'mean every month", 'Means')
line_chart_month

# 绘制周日均值
idx_weeks = dates.index('2017-12-11')
line_char_week = draw_line(
    weeks[1:idx_weeks], closes[1:idx_weeks], "closes'mean every week", 'Means')

# 绘制每周各天的日均值
wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_weeks]]
line_chart_weekday = draw_line(
    weekdays_int, closes[1:idx_weeks], "closes'mean every weekday", 'Mean')
line_chart_weekday.x_labels = wd
line_chart_weekday.render_to_file("closes'mean every weekday.svg")

# 将以上的五幅图整合在一起
with open('Closes Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>Close Dashboard</title><meta charset="utf8"></head><body>\n')
    for svg in ['closes.svg', 'closes_log10.svg', "closes'mean every month.svg",
                "closes'mean every week.svg", "closes'mean every weekday.svg"]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')
