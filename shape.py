### SUPERCLASS FOR ALL THE SHAPES ###



from rectangleshape import rectangleshape
from squareshape import squareshape
from houseshape import houseshape
from paralellinesshape import paralellinesshape

class shape:
    
    def __init__(self, background, flattening, heightrange, widthrange, centered):
        self.background= background
        self.flatten = flattening
        self.hrange= heightrange
        self.wrange= widthrange
        self.centered = centered

    ## Generates one shape depending on which shape appears on the parameter
    def generateshape(self, tshape):

        if(tshape == "square"):
            sqrshape = squareshape(self.background, self.flatten, self.hrange, 
                                       self.wrange, self.centered)
            square = sqrshape.generateshape()
            return square


        

