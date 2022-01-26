### CLASS FOR A SQUARE SHAPE ###

from numpy.random import randint
import numpy as np


class squareshape:

    background=[]
    def __init__(self, size, flattening, heightrange, widthrange, centered):
        self.background = np.zeros((size,size))
        self.flattening= flattening 
        self.hrange=heightrange 
        self.wrange= widthrange
        self.centered = centered

    # Generates the square shape 
    def generateshape(self):
        range = [0,0]
        size= len(self.background)
        if (self.hrange[1] > self.wrange[1]):
            range[1]= self.hrange[1]
        
        else:
            range[1]= self.wrange[1]
        
        ## ESTABLISH THE MAXIMUM SIDE MEASURE
        if(range[1] > size):
            range[1]= size

        
        if (self.hrange[0] < self.wrange[0]):
            range[0]= self.wrange[0]
        
        else:
            range[0]= self.hrange[0]
        
        ## ESTABLISH THE MINIMUM SIDE MEASURE
        if(range[0] < 3):
            range[0]= 3
        
        print(range[0])
        print(range[1])
        sideMeasure = randint(low=range[0], high=range[1])
        center= 0
        # The shape must be cenetered on the background
        if (self.centered == 0):
            center = [int(size/2)-1,int(size/2)-1]
            
        # The shape must be random centered
        else:
            center_found = False
            while (not center_found):
                center = randint(low=int(sideMeasure/2), high= size-int(sideMeasure/2), size=2)
                if((center[0] - int(sideMeasure/2)) >= 0 and 
                (center[0] + int(sideMeasure/2)) <= size-2 and 
                (center[1] - int(sideMeasure/2)-1) >= 0 and 
                (center[1] + int(sideMeasure/2)+1) <= size-2):
                    break 
        
        pointx = center[0]-int(sideMeasure/2)
        pointy= center[1]-int(sideMeasure/2)
        
        # High line 
        i = 0
        while(i < sideMeasure):
            self.background[pointx][pointy] = 1
            pointy = pointy + 1
            i += 1           

        #Right side line
        i = 0
        while(i < sideMeasure):
            self.background[pointx][pointy] = 1
            pointx = pointx + 1
            i += 1    

        i = 0
        while(i < sideMeasure):
            self.background[pointx][pointy] = 1
            pointy = pointy - 1
            i += 1   

        i = 0
        while(i < sideMeasure):
            self.background[pointx][pointy] = 1
            pointx = pointx - 1
            i += 1    

        return self.background    


