import matplotlib.pyplot as g
squares = (0, 1, 4, 9, 16, 25)
g.plot(squares, linewidth=5)
g.title("Square Numbers", fontsize=24)
g.xlabel("values", fontsize=24)
g.ylabel("square of values", fontsize=24)
g.tick_params(axis="both", labelsize=14)
g.show()
