from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
import random


x_initial_vel = random.random()
y_initial_vel = random.random()
z_initial_vel = random.random()


def gen(n):
    a = 0
    max = 10
    while a < max:
        yield np.array([np.cos(a), np.sin(a), a])
        a += max/n
        
        
        
n = random.random()
print(n)