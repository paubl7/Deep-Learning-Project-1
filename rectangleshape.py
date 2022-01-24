### CLASS FOR A RECTANGLE SHAPE ###

from numpy.random import Generator
from shape import shape

class rectangleshape(shape):
    
    def __init__(self, background, flattening, heightrange, widthrange, centered):
        super(rectangleshape, self).__init__(background, flattening, heightrange, widthrange,centered)