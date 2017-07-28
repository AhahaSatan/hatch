class Column:
    
    def __init__(self, position, disks, C):
        self.position = position
        self.disks = disks
        self.ids = []
        for k in range(len(self.disks)):
            self.ids.append(self.display_disk(self.disks[k], C, k))

    def can_add(self, column):
        return len(self.disks)==0 or (len(column.disks)>0 and self.disks[-1] > column.disks[-1])

    def add(self, disk, C):
        k = len(self.disks)
        self.ids.append(self.display_disk(disk, C, k))
        self.disks.append(disk)

    def remove(self, C):
        C.delete(self.ids.pop())
        return self.disks.pop()

    def clear_all(self, C):
        while len(self.ids) > 0:
            C.delete(self.ids.pop())
            self.disks.pop()

    def display_disk(self, disk, C, k, currfill=""):
        sz = disk.size/2
       # height = C.winfo_height()
       # height = 300
        return C.create_rectangle(self.position-sz, 600-k*30, self.position+sz, 600-(k+1)*30, fill=currfill)
                                           
    #def display(self, C):
        #C.create_rectangle(0, 200, 200, 0, fill = "black")
        
         #   sz = self.disks[k]/2
          #  height = C.winfo_height()
           # C.create_rectangle(self.position-sz, height-k*10, self.position+sz, height-(k+1)*10, fill="black")
        
