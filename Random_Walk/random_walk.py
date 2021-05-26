from random import choice
import random
import matplotlib.pyplot as plt


class randomWalk():
    """随机生成漫步数据的类"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_distance * y_direction
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


random_walk = randomWalk(50000)
random_walk.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))
point_numbers = list(range(random_walk.num_points))
fig = plt.axes()
fig.get_xaxis().set_visible(False)
fig.get_yaxis().set_visible(False)
plt.scatter(random_walk.x_values, random_walk.y_values, c=point_numbers,
            cmap=plt.cm.Greens, s=14)
plt.scatter(0, 0, c='red', s=50)
plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='blue', s=50)
plt.show()
