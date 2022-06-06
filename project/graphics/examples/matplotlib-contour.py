import matplotlib.pyplot as plt
import numpy as np

#creating an equation for z based off of variables x,y
x, y = np.meshgrid(np.linspace(-10, 10), np.linspace(-10, 10))
z = 9*(x**2+1)+8*x-(y**2)
levels = np.linspace(np.min(z), np.max(z), 15)

#creating a contour graph based off the equation of z
plt.contour(x,y,z, levels=levels)


plt.xlabel("x")
plt.ylabel("y")
plt.title("Function of z(x,y)")

plt.savefig('images/matplotlib-contour.png', dpi=300)
plt.savefig('images/matplotlib-contour.pdf')
plt.savefig('images/matplotlib-contour.svg')
plt.show()