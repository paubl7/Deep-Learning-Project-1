### CLASS FOR A PARALEL LINES SHAPE ###

from numpy.random import Generator
from shape import shape

class paralellinesshape(shape):
    
    def __init__(self, background, flattening, heightrange, widthrange, centered):
        super(paralellinesshape, self).__init__(background, flattening, heightrange, widthrange,centered)
