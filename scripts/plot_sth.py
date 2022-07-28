#!/usr/bin/env python3
# https://matplotlib.org/

import matplotlib.pyplot as plt
import math

x = range(50)
y = [1 + math.sin(i/4) for i in x]

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x, y)

plt.savefig("plot.png")
