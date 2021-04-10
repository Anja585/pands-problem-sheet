# plottask.py
# This program displays a plot of the functions f(x)=x, g(x)=x** and h(x)=x*** in the range [0, 4] on the one set of axes
# Author: Anja Antolkovic

# import the modules
import numpy as np
import matplotlib.pyplot as plt

# defining variables
xpoints = np.array(range(0, 5))
fxpoints = xpoints 
gxpoints = xpoints * xpoints
hxpoints = xpoints * xpoints * xpoints

# plotting the function
plt.plot(xpoints, fxpoints, color = 'r', label = "x")
plt.plot(xpoints, gxpoints, color = 'b', label = "x squared")
plt.plot(xpoints, hxpoints, color = "g", label = "x cubed")

# labeling the plot
plt.xlabel("x")
plt.ylabel("y")

# adding the title
plt.title("Random plot")

# adding a legend
plt.legend()

# showing the plot
plt.show()

# saving the plot
plt.savefig('random_plot.png')

