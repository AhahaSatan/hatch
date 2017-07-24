import numpy as np
import math
class Mandelbrot:
    def __init__(self, x1, y1, x2, y2, ttx, tty):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = max(y1, y2), min(y1, y2)
        incx = (x2-x1)/ttx
        incy = (y2-y1)/tty
        self.ttx = ttx
        self.tty = tty
        self.itercount = 0
        self.values = [[x1+x*incx + 1j*(y1+y*incy) for y in range(tty+1)] for x in range(ttx+1)]
        self.curr = [[0 for i in range(tty+1)] for j in range(ttx+1)]
        self.set = [[0 for i in range(tty+1)] for j in range(ttx+1)]


    def getcolour(self, i, j):
        return (self.set[i][j] + 1 - math.log(math.log(abs(self.curr[i][j])))/math.log(2))/self.itercount

    
    def iter(self):
        self.itercount = self.itercount + 1
        for i in range(self.ttx+1):
            for j in range(self.tty+1):
                if self.set[i][j] == 0:
                    self.curr[i][j] = self.curr[i][j]**2 + self.values[i][j]
                    if abs(self.curr[i][j]) > 2:
                        self.set[i][j] = self.itercount
                        
