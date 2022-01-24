### CLASS FOR A SQUARE SHAPE ###

from numpy.random import randint
from shape import shape

class squareshape(shape):

    def __init__(self, background, flattening, heightrange, widthrange, centered):
        super(squareshape, self).__init__(
            background = background, 
            flattening= flattening, 
            hrange=heightrange, 
            wrange= widthrange,
            centered = centered)

    # Generates the square shape 
    def generateshape(self):
        range = [0,0]
        size= len(self.background)
        if (self.hrange[1] > self.wrange[1] ):
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

        sideMeasure = randint(low=range[0], high=range[1])
        center= 0
        # The shape must be cenetered on the background
        if (self.centered == 0):
            center = [int(size/2)-1,int(size/2)-1]
            
        # The shape must be random centered
        else:
            center_found = False
            while (not center_found):
                center = randint(low=0, high= size, size=2)
                if((center[0] - int(sideMeasure/2)) >= 0 and (center[0] + int(sideMeasure/2)) <= size):
                    break 
        
        if ()
        pointx = center[0]+int(sideMeasure/2)
        pointy= center[1]
        finished = False
        while (not finished):
            

        


