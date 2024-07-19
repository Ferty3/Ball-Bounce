import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
import numpy as np
import math


theta=70
u=9
incre=0.1
e=0.7
ball=[0,0,u*math.cos(theta/57.29),u*math.sin(theta/57.29),0,-9.81]

def f(x,y,vx,vy,ax,ay):
    global ball
    vy=vy+ay*incre
    x=x+vx*incre
    y=y+vy*incre
    if y<0:
        y*=-e
        vy*=-e
    ball=[x,y,vx,vy,ax,ay]

fig, ax = plt.subplots()

def update(frame):
    f(ball[0],ball[1],ball[2],ball[3],ball[4],ball[5])
    dot, =ax.plot(ball[0],ball[1],"ro")

anim = FuncAnimation(fig, update, frames = None)


fig.subplots_adjust(left=0.25, bottom=0.25)





plt.show()