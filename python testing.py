from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

def gen(n):
    a = 0
    max = 10
    while a < max:
        yield np.array([np.cos(a), np.sin(a), a])
        a += max/n

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

N = 100
data = np.array(list(gen(N))).T
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

# Setting the axes properties
ax.set_xlim3d([-3, 3])
ax.set_xlabel('X')

ax.set_ylim3d([-3, 3])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 10])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=20)
ani.save('matplot003.gif')
#plt.show()