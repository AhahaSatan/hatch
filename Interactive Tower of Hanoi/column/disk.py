class Disk:

    def __init__(self, rank, size):
        self.rank = rank
        self.size = size
    def __lt__(self, other):
        return self.rank < other.rank
    def __gt__(self, other):
        return self.rank > other.rank
    
