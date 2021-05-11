#%%
from matplotlib import pyplot as plt
import numpy as np

#%%
fig1, ax = plt.subplots()  # creat a figure containing a single axes
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # plot some data on the axes
fig2, axs = plt.subplots(2, 2)
fig3, (ax1, ax2) = plt.subplots(1, 2)
fig4, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# 通过不设置ax参数可以发现，plt.subplots(m, n)就是创建一个有m*n个小图的空图，默认x-y平面图，横纵坐标长度为1,刻度为0.2
# The figure keeps track of all the child Axes, a smattering of 'special' artists (titles, figure legends, etc), and the canvas.
# The Axes contains two (or three in the case of 3D) Axis objects (be aware of the difference between Axes and Axis)
# %%
# for each Axes(matplotlib.axes.Axes) graph method, there is a corresponding function in the matplotlib.pyplot module
# 因此上面的例子也可以简写为
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# %%
# easiest way to create a new figure is with pyplot
fig = plt.figure() # an empty figure with no Axes
fig, ax = plt.subplots() # a figure with a single Axes
fig, axs = plt.subplots(2, 2) # a figure with a 2*2 grid of Axes

# %%
