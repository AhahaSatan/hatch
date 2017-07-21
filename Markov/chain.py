from textparser import Parser
from collections import defaultdict
import random
class Chain:
    def __init__(self):
        
        self.p = Parser([])
        self.d = defaultdict(list)
        self.st = defaultdict(list)
        self.stvals = []
        
    def addfile(self, filename):
        tp = self.p.parsefile(filename)
        for i in tp:
            if len(i) > 1:
                self.st[i[0]].append(i[1])
                self.stvals.append(i[0])
            for j in range(1, len(i)-1):
                self.d[tuple(i[j-1:j+1])].append(i[j+1])

    def makeline(self):
        s = random.choice(self.stvals)
        l = [s, random.choice(self.st[s])]
        dn = {}
        while True:
            if tuple(l[-2:]) not in self.d or (l[-1][-1] in ["!", ".", "?"]):
                break
            else:
                f = tuple(l[-2:])
                if f not in dn:
                    dn[f] = self.d[f][:]
                if (len(dn[f]))==0: break
                else:
                    a = random.choice(dn[f])
                    dn[f].remove(a)
                    l.append(a)
        return " ".join(l)+" "

        
    
