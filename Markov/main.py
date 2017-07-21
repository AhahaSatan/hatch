
from findfile import Findfile
from chain import Chain
import os
import tkinter
from display import Display


c = Chain()
for i in ["texts\\"+i for i in os.listdir("texts")]:
    c.addfile(i)
Display()
