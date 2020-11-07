import numpy as np


R = np.linspace(0, 1.25, 100)

u = np.linspace(0,  2*np.pi, 800)

x = np.outer(R, np.cos(u))
y = np.outer(R, np.sin(u))
