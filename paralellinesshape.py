### CLASS FOR A PARALEL LINES SHAPE ###

from numpy.random import randint
import numpy as np

class paralellinesshape:
    
    background=[]
    def __init__(self, size, flattening, heightrange, widthrange, centered):
        self.background = np.zeros((size,size))
        self.flattening= flattening 
        self.hrange=heightrange 
        self.wrange= widthrange
        self.centered = centered
    
    def generateshape(self):
        pass
