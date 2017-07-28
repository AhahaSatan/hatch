class Board:

    def __init__(self, board, hashval):
        self.board = board
        self.hash = hashval

    def getcopy(self):
        return [i[:] for i in self.board]

    def streaklength(self, column, row, diry, player, length):
        #if row<0 or len(self.board[column])<=row: return 0
        if (row < 0 or column < 0 or column > 6 or len(self.board[column])<= row): return 0
        for i in range(length):
            if (row < 0 or column < 0 or column > 6
                or len(self.board[column])<= row
                or self.board[column][row]!=player):
                return False
            column += 1
            row += diry
        else:
            return True
    def threats(self, player):
        number = 0
        for i in range(7):
            tp = len(self.board[i])
            if tp>2 and tp<6:
                for j in self.board[i][-3:]:
                    if j!=player: break
                else:
                    number += 1
                    tp += 1
            for j in range(tp, 6):
                for k in range(-1, 2):
                    
                    if (self.streaklength(i+1, j+k, k, player, 3)
                    or self.streaklength(i-3, j+k*3, k, player, 3)
                    or (self.streaklength(i-1, j-k, k, player, 1)
                    and self.streaklength(i+1, j+k, k, player, 2))
                    or (self.streaklength(i-2, j-k*2, k, player, 2)
                    and self.streaklength(i+1, j+k, k, player, 1))):
                        number +=1
            
        return number
                    
    def eval(self):
        for i in range(7):
            if len(self.board[i])<4: continue
            p = self.board[i][-1]
            #print("p",p)
            for j in self.board[i][-4:]:
                if j!= p:
                    #print("j",j)
                    break
            else:
                return p*9999998
        for j in range(4):
            for k in range(len(self.board[j])):
                for i in range(-1, 2):
                    if self.streaklength(j, k, i, self.board[j][k], 4):
                        return self.board[j][k]*9999998
        else:
            return self.threats(1) - self.threats(-1)

    def moves(self):
        l = []
        for i in range(7):
            if len(self.board[i])<6: l.append(i)
        return l
