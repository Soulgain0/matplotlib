import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
            edgecolor='none', s=100)
plt.title("Square Numbers", fontsize=18)
plt.xlabel("values", fontsize=18)
plt.ylabel("square of values", fontsize=18)
plt.tick_params(axis="both", labelsize=10)
plt.axis([0, 1100, 0, 1100000])
plt.savefig("squares_plot.png")
plt.show()
