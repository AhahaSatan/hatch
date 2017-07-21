import numpy as np
import cv2 as cv
import time
import math
import os
from mandelbrot import Mandelbrot
gmx = 700
ttx = gmx
tty = int(gmx*2/3)
image = np.zeros((tty, ttx, 3), np.uint8)
cv.namedWindow("poop")
ccolour = 255
x1, y1 = 0, 0
cnumber = 1
started = False
os.makedirs("captures", exist_ok = True)

m = Mandelbrot(-2, 1, 1, -1, ttx, tty)
def save():
    global cnumber
    while "img"+str(cnumber)+".png" in os.listdir("captures"): cnumber = cnumber + 1
    cv.imwrite("captures\\img"+str(cnumber)+".png", image)

def makenew(x1, y1, x2, y2):
  #  print(x1, y1, x2, y2)
    global ttx, tty, m, image
    if x1 != x2 and y1 != y2:
        # ttx/tty == abs(x1-x2)/abs(y1-y2)
        # or tty/ttx == abs(y1-y2)/abs(x1-x2)
        if abs(x1-x2) > abs(y1-y2):
            ttx = gmx
            tty = int(gmx*abs(y1-y2)/abs(x1-x2))
        else:
            tty = gmx
            ttx = int(gmx*abs(x1-x2)/abs(y1-y2))
        z1 = m.values[x1][y1]
        z2 = m.values[x2][y2]
        m = Mandelbrot(z1.real, z1.imag, z2.real, z2.imag, ttx, tty)
        image = np.zeros((tty, ttx, 3), np.uint8)
    cv.imshow("poop", image)
    s = cv.waitKey(0)
    #print(s)
    if s == 115: save()
    update()
    
def select(event, x, y, flags, param):
    global x1, y1, started
    if event == cv.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        started = True
        
    elif event == cv.EVENT_LBUTTONUP:
        if started:
            started = False
            makenew(x1, y1, x, y)
            
    elif event == cv.EVENT_MOUSEMOVE:
        if started:
            im2 = np.copy(image)
            cv.rectangle(im2, (x1, y1), (x, y), (255, 0, 0), 1)
            cv.imshow("poop", im2)


cv.setMouseCallback("poop", select)
cv.imshow("poop", image)
#P^v(z)=log(n)*P^n/log|Zn|
#⇒ v(z) = logp(log(N)*P^n/log|Zn|)
#⇒ v(z) = logp(log(N)) + logp(P^n)- logp(log|Zn|)
#⇒ v(z) = n + logp(log(N))-logp(log|Zn|)
#⇒ v(z) = n + log(log(N)/log|Zn|)/log(P)
#⇒ v(z) = n - log(log|Zn|/log(N))/log(P)
#⇒ v(z) = n + log(log(N))/log(P) - log(log|Zn|)/log(P)
from colour import Color
blue = Color("blue")
black = Color("black")
red = Color("red")
white = Color("white")
colours = [[c.green*255, c.blue*255, c.red*255] for c in list(black.range_to(red, 50)) + list(red.range_to(white, 50))]#list(blue.range_to(red, 50)) + list(red.range_to(white, 50)) + list(white.range_to(blue, 50))]
def update():
    dn = False
    for k in range(500):
        m.iter()
        for i in range(ttx):
            for j in range(tty):
                if m.set[i][j] > 0:
                    c = m.getcolour(i,j)
            #        m.iter(i, j)
            
                  #  c = Color(hsl=(m.getcolour(i, j), 1, 0.5))
                  
                    image[j][i] = colours[int(c*100)%100]
                #    if c > 0.5: image[j][i] = [255, 255*c, 255*c]
                 #   else: image[j][i] = [255*c, 0, 0]
                    dn = True
        if dn: break
    #print(m.smoothmax)
    cv.imshow("poop", image)
    s = cv.waitKey(0)
    if s == 115: save()
    update()
print("Click and drag over area to zoom in")
print("Press 's' to save image, or any other key to iterate deeper")   
cv.waitKey(0)
update()
