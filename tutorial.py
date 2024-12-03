import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import math
#single points
axes=plt.axes(projection='3d')
x=np.arange(0,4*math.pi,0.01)
y=(np.arange(0,7,0.01)[0:len(x)])
x,y=np.meshgrid(x,y)
z=np.cos(x)

axes.plot_surface(x,y,z,cmap="plasma")
axes.view_init(azim=90,elev=0)
plt.show()
