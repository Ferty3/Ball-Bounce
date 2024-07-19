import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math

h=15

x = np.linspace(0, 25, 100)


def f(x, h):
    u=10
    g=9.81
    alpha=(2*g*h)/(u**2)
    theta=math.asin((1/((2+alpha)**0.5)))
    a=1/(2*((math.cos(theta/57.29))**2)*(((u**2)/g)))
    b=math.tan(theta)
    c=h

    return(-a*x ** 2 + b*x + c)


fig, ax = plt.subplots()
line, = ax.plot(x, f(x, h),lw=2)
floor, =ax.plot(x, [0]*100)

fig.subplots_adjust(left=0.25, bottom=0.25)

axx = fig.add_axes([0.25,.1,.65,.03])
heightslider = Slider(
    ax=axx,
    label='height',
    valmin=0,
    valmax=15,
    valinit=h,
)

def update(val):
    line.set_ydata(f(x, heightslider.val))
    fig.canvas.draw_idle()

heightslider.on_changed(update)
plt.show()