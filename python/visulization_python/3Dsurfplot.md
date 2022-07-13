# draw 3D surface plots with Matplotlib
ref:https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.16-3D-Surface-Plots/  
## [numpy.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy-meshgrid])
其实就是给定x轴y轴数据点，然后铺开为网格点坐标矩阵
```python
import numpy as np
x = np.linspace(-5, 5, 101) #numpy.linspace()函数用于在线性空间中以均匀步长生成数字序列。
y = np.linspace(-5, 5, 101)
# full coordinate arrays
xx, yy = np.meshgrid(x, y)
# xx.shape, yy.shape, zz.shape
# ((101, 101), (101, 101), (101, 101))
zz = np.sqrt(xx**2 + yy**2)
# sparse = True can be used to save memory and computation time
xs, ys = np.meshgrid(x, y, sparse=True)
zs = np.sqrt(xs**2 + ys**2)
# xs.shape, ys.shape, zs.shape
# ((1, 101), (101, 1), (101, 101))
# np.array_equal(zz, zs)
# True

import matplotlib.pyplot as plt
h = plt.contourf(x, y, zs) #绘制等高线
plt.axis('scaled') # Set equal scaling (i.e., make circles circular) by changing dimensions of the plot box. 
plt.colorbar()
plt.show()
```
![image](https://user-images.githubusercontent.com/52747634/178666301-7ee61c7d-84d6-4b8b-90b9-7fd51843fdb2.png)  
## 3D Surface Plots
>ax.plot_surface(X, Y, Z)  
>Where X and Y are 2D array of x and y points and Z is a 2D array of heights.  
```python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
#if using a Jupyter notebook, include:
#%matplotlib inline  #Ipython的魔法函数，功能是可以内嵌绘图，并且可以省略掉plt.show()这一步。

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
#Return coordinate matrices from coordinate vectors. meshgrid is very useful to evaluate functions on a grid
X,Y = np.meshgrid(x,y) 
Z = X*np.exp(-X**2 - Y**2)


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')


# Plot a 3D surface
ax.plot_surface(X, Y, Z)


plt.show()
```
![image](https://user-images.githubusercontent.com/52747634/178666614-34e8a0a4-c4c5-43c4-a19c-b3e2e76b3031.png)  

## Wire Frame Plots
>ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```python
import numpy as np
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = X * np.exp(-X**2 - Y**2)

# Plot a basic wireframe
# The keyword arguments rstride= and cstride= determine the row step size and the column step size. 
# These keyword arguments control how close together the "wires" in the wire frame plot are drawn.
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax1.set_title("row step size 10, column step  size 10")

ax2.plot_wireframe(X, Y, Z, rstride=20, cstride=20)
ax2.set_title("row step size 20, column step size 20")

plt.show()
```
![image](https://user-images.githubusercontent.com/52747634/178666856-f0113f9b-434e-45ef-9b2e-31e1b1faf037.png)
## Gradient Surface Plots
```python
 surf = ax.plot_surface(X, Y, Z, 
                         cmap=<color map>,
                         linewidth=0,
                         antialiased=False)
```
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111, projection='3d')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y, sparse=True)
Z = X*np.exp(-X**2 - Y**2)

# The keyword argument cmap=<color map> assigns the colors to the surface. 
# There is a wide array of color map options in Matplotlib. Options include 'coolwarm', 'gist_earth', and 'ocean'. 
# Find all of Matplotlib's colormaps in the Matplotlib documentation at matplotlib.org/tutorials/colors/colormaps. 
mycmap = plt.get_cmap('gist_earth')
ax1.set_title("gist_earth color map")
surf1 = ax1.plot_surface(X, Y, Z, cmap=mycmap)
# shrink 调整colorbar长度 shrink=0.5表示缩小一倍
# aspect: 调整colorbar宽度
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=20)

plt.show()
```
![image](https://user-images.githubusercontent.com/52747634/178667213-7ebc6b8d-0d19-4ef5-ad98-40fbaeadab17.png)

## 3D surface PLot with 2D Contour Plot Projections
```python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = X*np.exp(-X**2 - Y**2)


surf = ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.8, cmap=cm.ocean)
# zdir='z':将z轴压到xoy平面上，offset=np.min(Z):将图形映射到z=np.min(Z)的平面上
cset = ax.contourf(X, Y, Z, zdir='z', offset=np.min(Z), cmap=cm.ocean)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-5, cmap=cm.ocean)
cset = ax.contourf(X, Y, Z, zdir='y', offset=5, cmap=cm.ocean)

fig.colorbar(surf, ax=ax,  shrink=0.5, aspect=5)

ax.set_xlabel('X')
ax.set_xlim(-5, 5)
ax.set_ylabel('Y')
ax.set_ylim(-5, 5)
ax.set_zlabel('Z')
ax.set_zlim(np.min(Z), np.max(Z))
ax.set_title('3D surface with 2D contour plot projections')

plt.show()
```
![image](https://user-images.githubusercontent.com/52747634/178667356-e077dd9b-f661-42a9-bcf5-332bcaf78705.png)  

