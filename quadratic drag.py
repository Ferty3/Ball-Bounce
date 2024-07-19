import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math


theta=60
u=9
g=9.81
incre=0.1
c=0.5
A=0.1
d=1
h=10

x = np.linspace(0, 10, 100)

def f(theta,u,m):
    k=0.5*c*A*d/m
    vh=u*math.cos(theta/57.29)
    vv=u*math.sin(theta/57.29)
    xh=0
    xv=h
    coords=[[0],[h]]
    for i in range(0,30):
        print(k)
        ah=-vh*k*u
        av=-g-vv*k*u
        xh=xh+vh*incre+0.5*ah*incre**2
        xv=xv+vv*incre+0.5*av*incre**2
        vh=vh+ah*incre
        vv=vv+av*incre
        u=(vh**2+vv**2)**0.5
        coords[0].append(xh)
        coords[1].append(xv)
    return(coords)

def nodrag(x, theta,u):
    g=9.81
    a=1/(2*((math.cos(theta/57.29))**2)*(((u**2)/g)))
    b=math.tan(theta/57.29)
    c=h

    return(-a*x ** 2 + b*x + c)


fig, ax = plt.subplots()
coords=f(theta,u,0.1)
line, = ax.plot(coords[0], coords[1],lw=2)
line2, = ax.plot(x, nodrag(x, theta,u),lw=2)

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
    coords=f(angleslider.val,uslider.val,0.1)
    line.set_xdata(coords[0])
    line.set_ydata(coords[1])
    line2.set_ydata(nodrag(x, angleslider.val,uslider.val))
    fig.canvas.draw_idle()

angleslider.on_changed(update)
uslider.on_changed(update)
plt.show()