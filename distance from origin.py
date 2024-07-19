import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math


theta=30

t = np.linspace(0, 3, 100)


def f(t, theta):
    u=10
    g=9.81
    R=((u**2)*(t**2)-(u*math.sin(theta/57.29577)*(t**3)*(g))+0.25*(g**2)*(t**4))**0.5

    return(R)


fig, ax = plt.subplots()
line, = ax.plot(t, f(t, theta),lw=2)

fig.subplots_adjust(left=0.25, bottom=0.25)

axx = fig.add_axes([0.25,.1,.65,.03])
angleslider = Slider(
    ax=axx,
    label='theta',
    valmin=0,
    valmax=90,
    valinit=theta,
)


def update(val):
    line.set_ydata(f(t, angleslider.val))
    fig.canvas.draw_idle()

angleslider.on_changed(update)
plt.show()