# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []


fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1, xlim=(0, 2), ylim=(-4, 4))
ax2 = fig.add_subplot(2, 1, 2, xlim=(0, 2), ylim=(-4, 4))
line, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)


def init():



def update(buffer):

    return line,

fig1 = plt.figure()

data = np.random.rand(2, 100)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs=(data, l),
                                   interval=50, blit=True)

# To save the animation, use the command: line_ani.save('lines.mp4')

fig2 = plt.figure()

x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for add in np.arange(15):
    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
                                   blit=True)
# To save this second animation with some metadata, use the following command:
# im_ani.save('im.mp4', metadata={'artist':'Guido'})

fig = plt.figure()



plt.show()
