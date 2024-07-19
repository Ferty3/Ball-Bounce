import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math

theta=70
u=44
incre=0.01
h=10

planets=[[9.81,0,0,h,"red"],[9.81,50,50,10,"green"],[15,-20,60,5,"orange"]]

#determines direction of gravity
def gravity(planets,x,y):
    gx=0
    gy=0
    for i in planets:
        hyp=((i[1]-x)**2+(i[2]-y)**2)**0.5
        gx+=i[0]*(i[1]-x)/hyp
        gy+=i[0]*(i[2]-y)/hyp
    return([gx,gy])

#check if inside a planet
def checkcollide(planets,x,y):
    for i in planets:
        r2=(x-i[1])**2+(y-i[2])**2
        if r2<(i[3])**2:
            return(False)
    return(True)

#calculates path using time steps
def coords(theta,u):
    t=0
    heights=[[0],[h]]
    x=0
    y=h
    vx=u*math.cos(theta/57.29)
    vy=u*math.sin(theta/57.29)
    while checkcollide(planets,x,y):
        grav=gravity(planets,x,y)
        gx=grav[0]
        gy=grav[1]
        x=x+vx*incre-0.5*gx*incre**2
        y=y+vy*incre-0.5*gy*incre**2
        vx=vx+gx*incre
        vy=vy+gy*incre
        heights[0].append(x)
        heights[1].append(y)
        t+=incre
    return(heights)

def circle1(x,xc,yc,r):
    top=(r**2-(x-xc)**2)**0.5+yc
    return(top)

def circle2(x,xc,yc,r):
    bottom=-(r**2-(x-xc)**2)**0.5+yc
    return(bottom)
    

fig, ax = plt.subplots()
coord=coords(theta,u)
line, = ax.plot(coord[0], coord[1],lw=2)
for i in planets:
    x = np.linspace(i[1]-i[3], i[1]+i[3], 100)
    ax.plot(x, circle1(x,i[1],i[2],i[3]),i[4],lw=2)
    ax.plot(x, circle2(x,i[1],i[2],i[3]),i[4],lw=2)

fig.subplots_adjust(left=0.25, bottom=0.25)

axx = fig.add_axes([0.25,.1,.65,.03])
angleslider = Slider(
    ax=axx,
    label='theta',
    valmin=0,
    valmax=180,
    valinit=theta,
)

axu = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
uslider = Slider(
    ax=axu,
    label="u",
    valmin=1,
    valmax=50,
    valinit=u,
    orientation="vertical"
)

def update(val):
    coord=coords(angleslider.val,uslider.val)
    line.set_xdata(coord[0])
    line.set_ydata(coord[1])
    fig.canvas.draw_idle()

angleslider.on_changed(update)
uslider.on_changed(update)
plt.show()