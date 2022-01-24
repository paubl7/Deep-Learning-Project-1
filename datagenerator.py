### DATA GENERATOR CLASS ###

#This class is used to create the Data Generator of the project. 


#### IMPORTS

import os 
import sys
import argparse
import matplotlib as plt
import numpy as np
from shape import shape

class DataGenerator:

    def __init__(self, nimages, size, noise, flattening, minheight, maxheight, minwidth, maxwidth, centered, trainingsize, validationsize):
        self.nimages= nimages
        self.size= size 
        self.noise = noise
        self.flattening= flattening
        self.rangeheight= [minheight, maxheight]
        self.rangewidth= [minwidth, maxwidth]
        self.centered = centered
        self.trainingsize= trainingsize
        self.validationsize = validationsize
        self.testsize = trainingsize - validationsize
        

    #### PUBLIC FUNCTIONS ####

    ## Generates all the dataset

    def dataSetGenerator(): 
        pass

    #### PRIVATE FUNCTIONS ####

    ## Function to create a directory
    def __createDirectory(dir_name):
        dir_act= os.getcwd()
        dir_aux = dir_act + "/" + dir_name
        if (os.path.exists(dir_aux)):
            os.rmdir(dir_aux)

        os.mkdir(dir_aux + dir_aux)


    ## Function used to create the background of the image where the points will be distributed
    def __matrixCreation(size):
        matrix_aux=[]
        for a in range(size):
            aux= [False for i in range(size)]
            matrix_aux.append(aux)
        
        return matrix_aux


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nimages', default=250, type=int, help='Number of images that will be created')
    parser.add_argument('--size', default= 20, type = int,  help='Size of the matrix (size*size)')
    parser.add_argument('--noise', default= 0.4, type = float,  help='Probability for a pixel to be outside the shape (between 0 and 1)')
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
     

