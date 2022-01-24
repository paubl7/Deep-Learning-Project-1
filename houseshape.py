### CLASS FOR A HOUSE SHAPE ###

from numpy.random import Generator
from shape import shape

class houseshape(shape):
    
    def __init__(self, background, flattening, heightrange, widthrange, centered):
        super(houseshape, self).__init__(background, flattening, heightrange, widthrange,centered)
