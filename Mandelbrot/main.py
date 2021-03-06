import numpy as np
import cv2 as cv
import math
import os
from mandelbrot import Mandelbrot
gmx = 700
ttx = gmx
tty = int(gmx*2/3)
image = np.zeros((tty, ttx, 3), np.uint8)
cv.namedWindow("Mandelbrot")
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
        pviter = m.itercount
        m = Mandelbrot(z1.real, z1.imag, z2.real, z2.imag, ttx, tty)
        for i in range(pviter): m.iter()
        image = np.zeros((tty, ttx, 3), np.uint8)
        cv.imshow("Mandelbrot", image)
        update()
    else:
        s = cv.waitKey(0)
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
            cv.imshow("Mandelbrot", im2)


cv.setMouseCallback("Mandelbrot", select)
cv.imshow("Mandelbrot", image)
from colour import Color
blue = Color("blue")
black = Color("black")
red = Color("red")
white = Color("white")
colours = [[c.green*255, c.blue*255, c.red*255] for c in list(black.range_to(red, 50)) + list(red.range_to(white, 50))]#list(blue.range_to(red, 50)) + list(red.range_to(white, 50)) + list(white.range_to(blue, 50))]
def update():
    m.iter()
    for i in range(ttx):
        for j in range(tty):
            if m.set[i][j] > 0:
                c = m.getcolour(i,j)
                image[j][i] = colours[int(c*100)%100]
    cv.imshow("Mandelbrot", image)
    s = cv.waitKey(0)
    if s == 115: save()
    update()
print("Click and drag over area to zoom in")
print("Press 's' to save image, or any other key to iterate deeper")   
cv.waitKey(0)
update()
