### DATA GENERATOR CLASS ###

#This class is used to create the Data Generator of the project. 


#### IMPORTS

import os 
import argparse
from matplotlib.cbook import flatten
import numpy as np
from numpy import ndarray
from squareshape import squareshape
from rectangleshape import rectangleshape
from houseshape import houseshape
from paralellinesshape import paralellinesshape
from visualizator import visualizator

class DataGenerator:

    dataSetDirectory = ""
    answerstrain= []
    answersvalidation=[]
    answerstest = []

    def __init__(self, nimages, size, noise, flattening, minheight, maxheight, minwidth, maxwidth, centered, trainingsize, validationsize, visualize):
        self.nimages= nimages
        self.size= size 
        self.noise = noise
        self.flatten= flattening
        self.hrange= [minheight, maxheight]
        self.wrange= [minwidth, maxwidth]
        self.centered = centered
        self.trainingsize= trainingsize
        self.validationsize = validationsize + trainingsize
        self.visual = visualizator
        self.visualize = visualize
        

    #### PUBLIC FUNCTIONS ####

    ## Generates all the dataset

    def dataSetGenerator(self): 
        self.__createDirectory()
        self.__createDirectoriesTTV()
        filepath = os.path.join(self.dataSetDirectory, "train")
        print("Creating training data")
        section = 0
        for i in range(0, self.nimages):
            shape=[]
            answshape=0
            if(((i*self.nimages)/100 >= (self.nimages*self.trainingsize)/100) and section == 0):
                print("Creating validation data")
                section = 1
                filepath = os.path.join(self.dataSetDirectory, "validation")
                
            elif(((i*self.nimages/100) >= (self.nimages * self.validationsize)/100 )and section == 1):
                print("Creating test data")
                section = 2
                filepath = os.path.join(self.dataSetDirectory, "test")

            if(i%4 == 0):
                square= squareshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
                shape = square.generateshape()
                answshape = "1"
                
            elif(i%4 == 1):
                rectshape = rectangleshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
                shape = rectshape.generateshape()
                answshape = "2"

            elif(i%4 == 2):
                housesh = houseshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
                shape= housesh.generateshape()
                answshape = "3"
            else:
                linesshape = paralellinesshape(self.size, self.noise, self.hrange, 
                                       self.wrange, self.centered)
                shape = linesshape.generateshape()
                answshape = "4"

            self.__writedata(shape, i, filepath)

            if(section == 0):
                self.answerstrain.append(answshape)
            elif(section == 1):
                self.answersvalidation.append(answshape)
            else:
                self.answerstest.append(answshape)

            if (self.visualize == 1):
                self.visual.visualize_data_from_generator(self.visual, shape)
        
        print("DATASET CREATED")

    #### PRIVATE FUNCTIONS ####

    ## Function to create a directory
    def __createDirectory(self):
        dir_act= os.getcwd()
        dir_aux=os.path.join(dir_act,"dataset")
        dir_aux_num = os.path.join(dir_act,"dataset0")
        notcreated = True
        i=0
        while(notcreated):
            if (not os.path.exists(dir_aux_num)):
                self.dataSetDirectory = dir_aux_num
                os.mkdir(dir_aux_num)
                print("Directory: dataset", str(i), "created")
                notcreated = False
            
            i = i+1
            dir_aux_num = dir_aux + str(i)

    def __createDirectoriesTTV(self):
        trainDir= os.path.join(self.dataSetDirectory, "train")
        testDir= os.path.join(self.dataSetDirectory, "test")
        valDir= os.path.join(self.dataSetDirectory, "validation")
        os.mkdir(trainDir)
        os.mkdir(testDir)
        os.mkdir(valDir)


    def __writedata(self, matrix, i, filepath1):
        filename = "shape"+str(i)+".txt"
        filepath = os.path.join(filepath1, filename)
        image = "shape"+str(i)
        imagepath = os.path.join(filepath1, image)
        file = open(filepath, "w+")
        self.visual.save_data_from_generator(self.visual, matrix, imagepath)
        if(not self.flatten):
            matrix = ndarray.flatten(matrix)
            file.write(np.array2string(matrix))
        
        else:
            file.write(np.array2string(matrix))
            
        




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nimages', default=100, type=int, help='Number of images that will be created')
    parser.add_argument('--size', default= 20, type = int,  help='Size of the matrix (size*size) -> Minimum:10 Maximum:50')
    parser.add_argument('--noise', default= 0.04, type = float,  help='Probability for a pixel to be outside the shape (between 0 and 1)')
    parser.add_argument('--flattening', default= 1, type = bool,  help='Option to pass the data flattened or in a matrix form (0-> flattened, 1-> Matrix)')
    parser.add_argument('--minheight', default= 4, type = int, help= "Minimum height of the shapes" )
    parser.add_argument('--maxheight', default= 10, type= int, help= "Maximum height of the shapes"  )
    parser.add_argument('--minwidth', default= 4, type = int, help= "Minimum width of the shapes" )
    parser.add_argument('--maxwidth', default= 10, type= int, help= "Maximum width of the shapes" )
    parser.add_argument('--centered', default= 1, type= bool , help= "Option to have all the figures centered on the backgorund(0) or random centered (1)" )
    parser.add_argument('--trainingsize', default= 60, type = int, help= "Size of the training set in percentage (Test size = 100 - trainingsize - validationsize)" )
    parser.add_argument('--validationsize', default= 20, type = int, help= "Size of the validation set in percentage (Test size = 100 - trainingsize - validationsize)")
    parser.add_argument('--visualize', default = 0, type = bool, help= '0 if you do not want to visualize the data once is generated / 1 if you do want to (default = 0)' )
    args = parser.parse_args()

    dataGenerator= DataGenerator(args.nimages, args.size, args.noise, args.flattening, args.minheight, 
    args.maxheight, args.minwidth, args.maxwidth, args.centered, args.trainingsize, args.validationsize, args.visualize)
    
    dataGenerator.dataSetGenerator()



