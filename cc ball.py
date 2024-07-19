import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math


theta=60
u=9

x = np.linspace(0, 10, 100)


def f(x, theta,u):
    h=10
    g=9.81
    a=1/(2*((math.cos(theta/57.29))**2)*(((u**2)/g)))
    b=math.tan(theta/57.29)
    c=h

    return(-a*x ** 2 + b*x + c)


fig, ax = plt.subplots()
line, = ax.plot(x, f(x, theta,u),lw=2)

fig.subplots_adjust(left=0.25, bottom=0.25)

axx = fig.add_axes([0.25,.1,.65,.03])
angleslider = Slider(
    ax=axx,
    label='theta',
    valmin=0,
    valmax=80,
    valinit=theta,
)

axu = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
uslider = Slider(
    ax=axu,
    label="u",
    valmin=1,
    valmax=10,
    valinit=u,
    orientation="vertical"
)

def update(val):
    line.set_ydata(f(x, angleslider.val,uslider.val))
    fig.canvas.draw_idle()

angleslider.on_changed(update)
uslider.on_changed(update)
plt.show()