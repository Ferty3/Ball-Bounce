import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
import numpy as np
import math

Xcoord=80
Ycoord=80
m=1
g=9.81

x = np.linspace(0, 150, 100)

#this draws the path with minimum initial velocity
def minu(x,mult, X,Y):
    a=((X**2+Y**2)**0.5)/X**2
    b=(Y+(X**2+Y**2)**0.5)/X
    return(-a*x ** 2 + b*x)

#this draws the path with maximum range(45 degree angle)
def maxrange(x,mult,X,Y):
    u=mult*(g**0.5)*((Y+((X**2+Y**2)**0.5))**0.5)
    a=(g/(2*u**2))*(2)
    return(-a*x ** 2 + x)
#this draws the bounding parabola for all arcs
def bounding(x,mult,X,Y):
    u=max(mult*(g**0.5)*((Y+((X**2+Y**2)**0.5))**0.5),((4*Y**2+X**2)**0.5)*((2*g*Y)**0.5)/(2*Y))
    a=(g/(2*u**2))
    c=(u**2)/(2*g)
    return(-a*x ** 2 + c)
#this draws the minimum angle path with a velocity of the minimum times the multiplier
def lowball(x,mult,X,Y):
    u=mult*(g**0.5)*((Y+((X**2+Y**2)**0.5))**0.5)
    atan=-(g*X**2)/(2*u**2)
    btan=X
    ctan=-(g*X**2/(2*u**2))-Y
    tan=(-btan+(btan**2-4*atan*ctan)**0.5)/(2*atan)
    a=(g/(2*u**2))*(1+(tan)**2)
    b=tan
    return(-a*x ** 2 + b*x)
    
#this is the path that reaches the point at its peak
def peakball(x,mult,X,Y):
    u=((4*Y**2+X**2)**0.5)*((2*g*Y)**0.5)/(2*Y)
    a=(g/(2*u**2))*(1+((2*Y)/X)**2)
    b=(2*Y)/X
    return(-a*x ** 2 + b*x)
#this is the alternate angle for the peak ball to reach the point
def peakball2(x,mult,X,Y):
    u=((4*Y**2+X**2)**0.5)*((2*g*Y)**0.5)/(2*Y)
    atan=-(g*X**2)/(2*u**2)
    btan=X
    ctan=-(g*X**2/(2*u**2))-Y
    tan=(-btan-(btan**2-4*atan*ctan)**0.5)/(2*atan)
    a=(g/(2*u**2))*(1+(tan)**2)
    b=tan
    return(-a*x ** 2 + b*x)
#this is the alternate angle for the low ball to reach the point
def highball(x,mult,X,Y):
    u=mult*(g**0.5)*((Y+((X**2+Y**2)**0.5))**0.5)
    atan=-(g*X**2)/(2*u**2)
    btan=X
    ctan=-(g*X**2/(2*u**2))-Y
    tan=(-btan-(btan**2-4*atan*ctan)**0.5)/(2*atan)
    a=(g/(2*u**2))*(1+(tan)**2)
    b=tan
    return(-a*x ** 2 + b*x)

fig, ax = plt.subplots()
lineminu, = ax.plot(x, minu(x,m, Xcoord,Ycoord),lw=2)
linerange, = ax.plot(x, maxrange(x,m, Xcoord,Ycoord),lw=2)
linebounding, = ax.plot(x, bounding(x,m, Xcoord,Ycoord),lw=2)
linelowball, = ax.plot(x, lowball(x,m, Xcoord,Ycoord),lw=2)
linehighball, = ax.plot(x, highball(x,m, Xcoord,Ycoord),lw=2)
linepeakball, = ax.plot(x, peakball(x,m, Xcoord,Ycoord),lw=2)
linepeak2ball, = ax.plot(x, peakball2(x,m, Xcoord,Ycoord),lw=2)
floor, =ax.plot(x, [0]*100)
point, =ax.plot(Xcoord,Ycoord,"ro")
lines=[[lineminu,minu],[linerange,maxrange],[linebounding,bounding],[linelowball,lowball],[linehighball,highball],[linepeakball,peakball],[linepeak2ball,peakball2]]
toggles=[True,True,True,True,True,True,True]

fig.subplots_adjust(left=0.25, bottom=0.25)

#these sliders control the target point
axx = fig.add_axes([0.25,.15,.65,.03])
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

axm = fig.add_axes([0.25, 0.1, 0.65, 0.03])
mslider = Slider(
    ax=axm,
    label="multplier",
    valmin=1,
    valmax=1.5,
    valinit=m,
)

def update(val):
    for i in range(0,len(lines)):
        if toggles[i]:
            lines[i][0].set_ydata(lines[i][1](x,mslider.val, Xslider.val,Yslider.val))
        else:
            lines[i][0].set_ydata([0])
    point.set_xdata(Xslider.val)
    point.set_ydata(Yslider.val)
    fig.canvas.draw_idle()


#buttons to toggle on and off lines
def toggle1(val):
    toggles[0]=not toggles[0]
    update
    
def toggle2(val):
    toggles[1]=not toggles[1]
    update
    
def toggle3(val):
    toggles[2]=not toggles[2]
    update
    
def toggle4(val):
    toggles[3]=not toggles[3]
    update
    
def toggle5(val):
    toggles[4]=not toggles[4]
    update
    
def toggle6(val):
    toggles[5]=not toggles[5]
    update
    
def toggle7(val):
    toggles[6]=not toggles[6]
    update
        
       
ax1 = fig.add_axes([0.1, 0.05, 0.1, 0.05])
ax2 = fig.add_axes([0.2, 0.05, 0.1, 0.05])
ax3 = fig.add_axes([0.3, 0.05, 0.1, 0.05])
ax4 = fig.add_axes([0.4, 0.05, 0.1, 0.05])
ax5 = fig.add_axes([0.5, 0.05, 0.1, 0.05])
ax6 = fig.add_axes([0.6, 0.05, 0.1, 0.05])
ax7 = fig.add_axes([0.7, 0.05, 0.1, 0.05])
bn1 = Button(ax1, 'minu')
bn2 = Button(ax2, 'range')
bn3 = Button(ax3, 'bounding')
bn4 = Button(ax4, 'lowball')
bn5 = Button(ax5, 'highball')
bn6 = Button(ax6, 'peak')
bn7 = Button(ax7, 'high peak')



bn1.on_clicked(toggle1)
bn2.on_clicked(toggle2)
bn3.on_clicked(toggle3)
bn4.on_clicked(toggle4)
bn5.on_clicked(toggle5)
bn6.on_clicked(toggle6)
bn7.on_clicked(toggle7)

Xslider.on_changed(update)
Yslider.on_changed(update)
mslider.on_changed(update)
plt.show()
