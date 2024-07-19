import matplotlib.pyplot as plt
import pygame, requests
import pygame.image
import io
import numpy as np
import math
import time

g=9.81
theta=70
u=15
r=52
m=25
incre=1/24
ev=0.8
eh=0.6
rad=-12
k=0.0147
init=[0,0,u*math.cos(theta/57.29),u*math.sin(theta/57.29),0,-g,0,rad]
ball=[0,0,u*math.cos(theta/57.29),u*math.sin(theta/57.29),0,-g,0,rad]
v=u
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, -angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    return rot_image

def convertcoords(image,x,y):
    w=image.get_width()
    h=image.get_height()
    X=x-(w/2)
    Y=y-(h/2)
    return([X,Y])

def ballcoord(x,y,vx,vy,ax,ay,theta,rad):
    global ball
    v=(vx**2+vy**2)**0.5
    ax=-vx*k*v
    ay=-g-vy*k*v
    vy+=ay*incre
    vx+=ax*incre
    x+=vx*incre
    y+=vy*incre
    if y<0:
        if abs(rad)<0.5:
            rad=r*vx/(3*m)
        else:
            vx=2*r*rad*(1+eh)/(7*m)
            rad*=-(2-5*eh)/7
        y*=-ev
        vy*=-ev
    if r+m*y>550:
        if abs(rad)<0.5:
            rad=-r*vx/(3*m)
        else:
            vx=2*r*rad*(1+eh)/(7*m)
            rad*=-(2-5*eh)/7
        inset=(r+y*m)-550
        y=(550-r-inset*ev)/m
        vy*=-ev
    if x<0:
        if abs(rad)<0.5:
            rad=r*vy/(3*m)
        else:
            vy=2*r*rad*(1+eh)/(7*m)
            rad*=-(2-5*eh)/7
        x*=-ev
        vx*=-ev
    if r+m*x>750:
        if abs(rad)<0.5:
            rad=-r*vy/(3*m)
        else:
            vy=2*r*rad*(1+eh)/(7*m)
            rad*=-(2-5*eh)/7
        inset=(r+x*m)-750
        x=(750-r-inset*ev)/m
        vx*=-ev
    theta=(theta+rad*incre*57.29)%360
    ball=[x,y,vx,vy,ax,ay,theta,rad]


pygame.init()


window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))


ballimage = requests.get('https://github.com/Ferty3/Ball-Bounce/blob/main/ball.png?raw=true').content
ballimage = io.BytesIO(ballimage)

ballimage=pygame.image.load(ballimage)


running = True
while running:
    window.fill("white")
    ballcoord(ball[0],ball[1],ball[2],ball[3],ball[4],ball[5],ball[6],ball[7])
    rotatedball = rot_center(ballimage, ball[6])
    cc=convertcoords(rotatedball,r+m*ball[0],600-r-m*ball[1])
    window.blit(rotatedball, (cc[0], cc[1]))
    pygame.display.update()
    time.sleep(incre)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running=False
            if event.key == pygame.K_RIGHT:
                ball=init
            if event.key == pygame.K_UP:
                init=ball