import random
from board import Board
class Ai:
    def __init__(self, depth):
        self.depth = depth
        self.bestmove = -1
        self.dn = [{} for i in range(depth+1)]
        self.hashvals = [[[random.randint(1, 1000000000) for i in range(3)] for j in range(6)] for k in range(7)]

    def negamax(self, state, cdepth, alpha, beta, player):
        if state.hash in self.dn[cdepth]:
            #print(state.hash, self.dn[cdepth][state.hash])
            return self.dn[cdepth][state.hash]
        if cdepth == 0:
            #print(state.eval(), player, cdepth, state.board)
            return state.eval()*player
        elif abs(state.eval())== 9999998:
            #print(state.eval(), player, cdepth)
            return state.eval()*player
        best = -9999999
        pvrand = 0
        for i in state.moves():
            tp = state.getcopy()
            tphash = state.hash^self.hashvals[i][len(tp[i])][1]^self.hashvals[i][len(tp[i])][1+player]
            tp[i].append(player)
            q = -self.negamax(Board(tp, tphash), cdepth-1, -beta, -alpha, -player)
            #if q!=0: print(q, player, cdepth, i)
            if q>best:
                best = q
                if cdepth == self.depth: self.bestmove = i
            elif q==best and cdepth==self.depth:
                tprand = random.random()
                if tprand>pvrand:
                    pvrand = tprand
                    self.bestmove = i
            alpha = max(alpha, q)
            if alpha > beta:
                break
        self.dn[cdepth][state.hash]=best
        return best
                


    
