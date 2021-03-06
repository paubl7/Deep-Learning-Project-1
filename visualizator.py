### VISUALIZATOR CLASS ###

import matplotlib.pyplot as plt
from matplotlib import cm

class visualizator:
    
    def __init__():
        pass

    def visualize_data_from_generator(self, matrix):
        plt.imshow(matrix, interpolation = 'nearest')
        plt.show()

    def save_data_from_generator(self,matrix,name):
        plt.imshow(matrix, interpolation = 'nearest')
        plt.savefig(name, bbox_inches='tight')