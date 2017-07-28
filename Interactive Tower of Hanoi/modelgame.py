from gamescreen import Gamescreen
class Modelgame:
    def __init__(self, screen):
        self.columns = [[i.rank for i in j.disks] for j in screen.l]

    def get_index(self, val):
        for i in range(3):
            for j in self.columns[i]:
                if j == val: return i

    def move(self, col1, col2):
        self.columns[col2].append(self.columns[col1].pop())
