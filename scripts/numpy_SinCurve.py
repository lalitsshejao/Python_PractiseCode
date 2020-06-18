import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot

x=np.arange(0, 3*np.pi, 0.1)
# y=np.sin(x)
# y=np.cos(x)
y=np.tan(x)

plt.plot(x,y)
plt.show()