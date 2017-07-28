import math
from functools import reduce
import random
class Nim:
    def __init__(self, ncols):
        self.piles = [random.randint(1, 20) for i in range(ncols)]
        self.xorsum = reduce((lambda x, y: x^y), self.piles)

    def move(self, col, num):
        self.xorsum^=self.piles[col]^num
        self.piles[col]=num

    def bestmove(self):
        if self.xorsum == 0:
            for i in range(len(self.piles)):
                if self.piles[i]!=0:
                    t = tuple([i, random.randint(0, self.piles[i]-1)])
                    return t
        maxbit = int(math.log2(self.xorsum))
        tt = 0
        for i in range(len(self.piles)):
            if self.piles[i]&(1<<maxbit) > 0:
                for j in range(maxbit, -1, -1):
                    if (self.piles[i]&(1<<j))>0:
                        if self.xorsum&(1<<j) >0:
                            tt+=(1<<j)
                    elif self.xorsum&(1<<j)>0:
                        tt-=(1<<j)
                return tuple([i, self.piles[i]-tt])
