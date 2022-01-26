### CLASS FOR A RECTANGLE SHAPE ###

from numpy.random import randint
import numpy as np

class rectangleshape:
    
    background=[]
    def __init__(self, size, noise, heightrange, widthrange, centered):
        self.background = np.zeros((size,size))
        self.noise= noise 
        self.hrange=heightrange 
        self.wrange= widthrange
        self.centered = centered

    
    def generateshape(self):
        size = len(self.background)

        if(self.hrange[0] < 2):
            self.hrange[0] = 2
        
        if (self.hrange[1] > size):
            self.hrange[1] = size
        
        if(self.wrange[0] < 2):
            self.wrange[0] = 2
        
        if (self.wrange[1] > size):
            self.wrange[1] = size
        
        hsize = randint(low=self.hrange[0], high= self.hrange[1])
        wsize = randint(low=self.wrange[0], high= self.wrange[1])

        bigSizeMeasure= hsize
        lowSizeMeasure = wsize
        if(hsize < wsize):
            bigSizeMeasure = wsize
            lowSizeMeasure = hsize

        # The shape must be cenetered on the background
        if (self.centered == 0):
            center = [int(size/2)-1,int(size/2)-1]

        else:
            center_found = False
            while (not center_found):
                center = randint(low=int(lowSizeMeasure/2), high= size-int(bigSizeMeasure/2), size=2)
                if((center[0] - int(wsize/2)) >= 0 and 
                (center[0] + int(wsize/2)) <= size-2 and 
                (center[1] - int(hsize/2)-1) >= 0 and 
                (center[1] + int(hsize/2)+1) <= size-2):
                    break 
            
        pointx= center[0]-int(hsize/2)
        pointy= center[1]-int(wsize/2)

        # High line 
        i = 0
        while(i < wsize):
            self.background[pointx][pointy] = 1
            pointy = pointy + 1
            i += 1           

        #Right side line
        i = 0
        while(i < hsize):
            self.background[pointx][pointy] = 1
            pointx = pointx + 1
            i += 1    

        i = 0
        while(i < wsize):
            self.background[pointx][pointy] = 1
            pointy = pointy - 1
            i += 1   

        i = 0
        while(i < hsize):
            self.background[pointx][pointy] = 1
            pointx = pointx - 1
            i += 1    

        return self.background 