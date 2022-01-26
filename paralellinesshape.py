### CLASS FOR A PARALEL LINES SHAPE ###

from numpy.random import randint
import numpy as np

class paralellinesshape:
    
    background=[]
    def __init__(self, size, noise, heightrange, widthrange, centered):
        self.background = np.zeros((size,size))
        self.noise= noise
        self.hrange=heightrange 
        self.wrange= widthrange
        self.centered = centered
    
    def generateshape(self):
        size = len(self.background)
        
        if(self.hrange[0] < 1):
            self.hrange[0] = 1

        if (self.hrange[1] > size):
            self.hrange[1] = size
        
        if(self.wrange[0] < 1):
            self.wrange[0] = 1
        
        if (self.wrange[1] > size-2):
            self.wrange[1] = size-2
        
        hsize = randint(low=self.hrange[0], high= self.hrange[1])
        wsize = randint(low=self.wrange[0], high= self.wrange[1])

        # The shape must be cenetered on the background
        if (self.centered == 0):
            center = [int(size/2)-1,int(size/2)-1]

        else:
            center_found = False
            while (not center_found):
                center = randint(low=int(hsize/2), high= size-int(wsize/2), size=2)
                if((center[0] - int(hsize/2)) >= 0 and 
                (center[0] + int(hsize/2)) <= size-2 and 
                (center[1] - int(wsize/2)-1) >= 0 and 
                (center[1] + int(wsize/2)+1) <= size-2):
                    break 
            
        pointx= center[0]-int(hsize/2)
        pointy= center[1]-int(wsize/2)

        #First Line
        i = 0
        while(i < hsize):
            self.background[pointx][pointy] = 1
            pointx = pointx + 1
            i += 1           

        #Right side line
        i = 0
        pointx = pointx - hsize
        pointy = pointy + wsize +1
        while(i < hsize):
            self.background[pointx][pointy] = 1
            pointx = pointx + 1
            i += 1    
        
        return self.background
