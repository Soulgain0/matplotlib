import pygal
from random import randint


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


"""模拟掷骰子"""
die_1 = Die()
die_2 = Die(10)
results = []
for roll_number in range(1000):
    results.append(die_1.roll() + die_2.roll())
# print(results)
"""计算骰子掷出各点数的总次数"""
frequencies = []
x_labels = []
for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequencies.append(results.count(value))
    x_labels.append(str(value))
print(frequencies)
"""绘制直方图"""

hist = pygal.Bar()
hist.title = "Results of rolling selected dies 1000 times"
hist.x_labels = x_labels
hist.x_title = "results"
hist.y_title = "frequecies"
hist.add('D6 + D6', frequencies)
hist.render_to_file('two_dies.svg')
