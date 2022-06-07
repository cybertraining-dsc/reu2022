import matplotlib.pyplot as plt

x = range(0,4)
y = x
plt.plot(x,y)

# Rotating Ticks
plt.xticks(rotation=90)
plt.yticks(rotation=45)

plt.xlabel('x values')
plt.ylabel('y values')
plt.title(r'$y=x$')
plt.savefig('images/matplotlib-rotatingticks.svg')
plt.show()