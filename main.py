from operator import ge
import numpy as np
import string
import network as nt
import datagenerator as dg
import argparse
import os


generated_network = nt.network()

def add_layer(self, layer_type, n_neurons, act_function, wtype, wrl, wrh, brl, brh, ouput_type):
    if(layer_type== 0):
        generated_network.add_input_layer()

    elif (layer_type == 1):
        generated_network.add_hidden_layer()

    elif (layer_type == 2):
        generated_network.add_output_layer()

def document_parser ():
    pass


    


if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--config', default=10, type=string, help='path of the configuration document')
    #parser.add_argument('--data', default='/dataset0', type=string, help='path of the dataset')
    #parser.add_argument('--data', default='/dataset0', type=string, help='path of the dataset')

    data = np.array=[[0,0,0,0,0,0],
                     [0,1,1,1,0,0]
                     [0,1,0,1,0,0]
                     [0,1,1,1,0,0]
                     [0,0,0,0,0,0]
                     [0,0,0,0,0,0]]
    generated_network = nt.network('MSE', 0.01, -0.01, 0.01, 'range', data)