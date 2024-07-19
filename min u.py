import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math

Xcoord=80
Ycoord=80

x = np.linspace(0, 150, 100)


def f(x, X,Y):
    g=9.81
    theta=math.atan((Y+(X**2+Y**2)**0.5)/X)
    u=(g**0.5)*((Y+(X**2+Y**2)**0.5)**0.5)
    a=1/(2*((math.cos(theta))**2)*(((u**2)/g)))
    b=math.tan(theta)

    return(-a*x ** 2 + b*x)


fig, ax = plt.subplots()
line, = ax.plot(x, f(x, Xcoord,Ycoord),lw=2)
point, =ax.plot(Xcoord,Ycoord,"ro")


fig.subplots_adjust(left=0.25, bottom=0.25)

axx = fig.add_axes([0.25,.1,.65,.03])
Xslider = Slider(
    ax=axx,
    label='Xcoord',
    valmin=0,
    valmax=80,
    valinit=Xcoord,
)

axu = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
Yslider = Slider(
    ax=axu,
    label="Ycoord",
    valmin=0,
    valmax=80,
    valinit=Ycoord,
    orientation="vertical"
)

def update(val):
    line.set_ydata(f(x, Xslider.val,Yslider.val))
    point.set_xdata(Xslider.val)
    point.set_ydata(Yslider.val)
    fig.canvas.draw_idle()

Xslider.on_changed(update)
Yslider.on_changed(update)
plt.show()