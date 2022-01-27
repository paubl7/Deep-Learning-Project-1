### DATA GENERATOR CLASS ###

#This class is used to create the Data Generator of the project. 


#### IMPORTS

import os 
import argparse
import matplotlib as plt
import numpy as np
from squareshape import squareshape
from rectangleshape import rectangleshape
from houseshape import houseshape
from paralellinesshape import paralellinesshape
from visualizator import visualizator

class DataGenerator:

    def __init__(self, nimages, size, noise, flattening, minheight, maxheight, minwidth, maxwidth, centered, trainingsize, validationsize):
        self.nimages= nimages
        self.size= size 
        self.noise = noise
        self.flatten= flattening
        self.hrange= [minheight, maxheight]
        self.wrange= [minwidth, maxwidth]
        self.centered = centered
        self.trainingsize= trainingsize
        self.validationsize = validationsize
        self.testsize = trainingsize - validationsize
        self.visual = visualizator
        

    #### PUBLIC FUNCTIONS ####

    ## Generates all the dataset

    def dataSetGenerator(self): 
        
        for i in range(0, self.nimages):
            if(i%4 == 0):
                shape= self.generateshapedata("square")
            elif(i%4 == 1):
                shape= self.generateshapedata("rectangle")
            elif(i%4 == 2):
                shape = self.generateshapedata("lines")
            else:
                shape = self.generateshapedata("house")

            self.visual.visualize_data_from_generator(self.visual, shape)


    ## Generates one shape depending on which shape appears on the parameter
    def generateshapedata(self, tshape):
        if(tshape == "square"):
            sqrshape = squareshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
            square = sqrshape.generateshape()
            return square
        
        if (tshape == "rectangle"):
            rectshape = rectangleshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
            rectangle = rectshape.generateshape()
            return rectangle
        
        if (tshape == "house"):
            housesh = houseshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
            house= housesh.generateshape()
            return house

        if (tshape == "lines"):
            lineshape = paralellinesshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
            lines = lineshape.generateshape()
            return lines


    #### PRIVATE FUNCTIONS ####

    ## Function to create a directory
    def __createDirectory(dir_name):
        dir_act= os.getcwd()
        dir_aux = dir_act + "/" + dir_name
        if (os.path.exists(dir_aux)):
            os.rmdir(dir_aux)

        os.mkdir(dir_aux + dir_aux)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nimages', default=10, type=int, help='Number of images that will be created')
    parser.add_argument('--size', default= 20, type = int,  help='Size of the matrix (size*size) -> Minimum:10 Maximum:50')
    parser.add_argument('--noise', default= 0.04, type = float,  help='Probability for a pixel to be outside the shape (between 0 and 1)')
    parser.add_argument('--flattening', default= 0, type = bool,  help='Option to pass the data flattened or in a matrix form (0-> flattened, 1-> Matrix)')
    parser.add_argument('--minheight', default= 4, type = int, help= "Minimum height of the shapes" )
    parser.add_argument('--maxheight', default= 10, type= int, help= "Maximum height of the shapes"  )
    parser.add_argument('--minwidth', default= 4, type = int, help= "Minimum width of the shapes" )
    parser.add_argument('--maxwidth', default= 10, type= int, help= "Maximum width of the shapes" )
    parser.add_argument('--centered', default= 1, type= bool , help= "Option to have all the figures centered on the backgorund(0) or random centered (1)" )
    parser.add_argument('--trainingsize', default= 60, type = int, help= "Size of the training set (Test size = 100 - trainingsize - validationsize)" )
    parser.add_argument('--validationsize', default= 20, type = int, help= "Size of the validation set (Test size = 100 - trainingsize - validationsize)")

    args = parser.parse_args()

    dataGenerator= DataGenerator(args.nimages, args.size, args.noise, args.flattening, args.minheight, 
    args.maxheight, args.minwidth, args.maxwidth, args.centered, args.trainingsize, args.validationsize)
    
    dataGenerator.dataSetGenerator()



