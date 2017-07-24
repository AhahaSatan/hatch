from collections import defaultdict
class Matrix:
    def __init__(self):
        self.r = [[] for j in range(729)]
        self.c = [[] for j in range(324)]
        self.h = [0 for i in range(324)]
        self.ch = defaultdict(set)
        self.pvm = []
        cnt = 0
        #i -> row
        #j -> column
        #k -> number
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    clms = [i*9+j, 81+i*9+k, 162+j*9+k, 243+((i//3)*3 + j//3)*9 + k]
                    for l in clms:
                        self.h[l] += 1
                        self.r[cnt].append(l)
                        self.c[l].append(cnt)
                    cnt += 1
        for i in range(324):
            self.ch[self.h[i]].add(i)
            
    def removerow(self, row, column):
        for c in self.r[row]:
            if c!= column:
                self.c[c].remove(row)
                self.ch[self.h[c]].remove(c)
                self.h[c] -= 1
                self.ch[self.h[c]].add(c)

    def replacerow(self, row, column):
        for c in self.r[row]:
            if c != column:
                self.c[c].append(row)
                self.ch[self.h[c]].remove(c)
                self.h[c] += 1
                self.ch[self.h[c]].add(c)

    def removecolumn(self, row, column):
        for r in self.c[column]:
            if r != row:
                self.removerow(r, column)
        self.ch[self.h[column]].remove(column)
        self.ch[-1].add(column)
        
    def replacecolumn(self, row, column):
        for r in self.c[column]:
            if r != row:
                self.replacerow(r, column)
        self.ch[-1].remove(column)
        self.ch[self.h[column]].add(column)

    def addnumber(self, row, column, number):
        cvl = row*81 + column*9 + number - 1
        self.pvm.append(cvl)
        for c in self.r[cvl]:
            self.removecolumn(cvl, c)
        
    def solve(self):

        if len(self.ch[-1]) == 324: return True
        elif len(self.ch[0]) > 0: return False
        else:
            for i in range(1, 10):
                if len(self.ch[i]) == 0: continue
                else:
                    tp = self.ch[i].pop()
                    self.ch[-1].add(tp)
                    for nrow in self.c[tp]:
                        self.pvm.append(nrow)
                        for r in self.c[tp]:
                            if r != nrow: self.removerow(r, tp)
                            
                        for c in self.r[nrow]:
                            if c!= tp:
                                self.removecolumn(nrow, c)
                        if self.solve():
                            return True
                        else:
                            self.pvm.pop()
                            for c in reversed(self.r[nrow]):
                                if c!= tp:
                                    self.replacecolumn(nrow, c)
                            for r in reversed(self.c[tp]):
                                if r != nrow: self.replacerow(r, tp)
                            
                            
                    self.ch[-1].remove(tp)
                    self.ch[i].add(tp)
                    return False
            return False

    def gensol(self):
        self.sol = [[0 for i in range(9)] for j in range(9)]
        for i in self.pvm:
            self.sol[i//81][(i%81)//9] = str((i%9)+1)

