import matplotlib.pyplot as plot
import math

def f(x):
    return x * (9 / 5) + 32

xs = range(-30, 110)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
